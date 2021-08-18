
import logging as log


class Point(object):

    def __init__(self, x, y):
        self.x, self.y = x, y

    def __str__(self):
        return "({}, {})".format(self.x, self.y)

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point((other.x < self.x) & (self.x - other.x), (other.y < self.y) & (self.y - other.y))

    def __truediv__(self, other):
        if other.x == 0:
            return Point(0, self.y / other.y)
        elif other.y == 0:
            return Point(self.x / other.x, 0)
        else:
            return Point(self.x / other.x, self.y / other.y)

    def __mul__(self, other):
        return Point(self.x * other, self.y * other)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


class CMDSeq(object):

    trans = {	"U": Point(0, 1),
              "D": Point(0, -1),
              "R": Point(1, 0),
              "L": Point(-1, 0)}

    def __init__(self, seq):
        self.seq = seq

        self.seq_delta = {k: 0 for k in 'LURD'}
        self.parse_cmdseq()

        self.hori_delta = self.seq_delta['R'] - self.seq_delta['L']
        self.vert_delta = self.seq_delta['U'] - self.seq_delta['D']
        self.delta = Point(self.hori_delta, self.vert_delta)

        self.max_hori_delta = max(self.seq_delta['R'], self.seq_delta['L'])
        self.max_vert_delta = max(self.seq_delta['U'], self.seq_delta['D'])

        self.loopback_factor = max(max(self.max_hori_delta - self.hori_delta, 0),
                                   max(self.max_vert_delta - self.vert_delta, 0))

        self.is_loop = self.hori_delta == self.vert_delta == 0

    def parse_cmdseq(self):
        """translates the cmd_seq to fill the seq_delta (counts how many moves in each direction)
        """
        for i in self.seq:
            self.seq_delta[i] += 1

    def repeat_ratio(self, point):
        return point / Point(self.hori_delta, self.vert_delta)

    def __str__(self):
        return "%s" % (self.seq)


def Robot():

    log.basicConfig(format='%(levelname)s:%(message)s', level=log.CRITICAL)

    end = Point(*[*list(map(int, input().split()))])
    log.debug('End point: %s.', end)

    cmd = CMDSeq(input())
    log.info('Command sequence: %s.', cmd.seq)
    log.info('Command sequence delta: (%s, %s).', cmd.hori_delta, cmd.vert_delta)
    log.debug('Command max hori delta: %s.', cmd.max_hori_delta)
    log.debug('Command max vert delta: %s.', cmd.max_vert_delta)
    log.debug('Command loopback ratio: %s.', cmd.loopback_factor)

    """	-If the end_point is at a totally different quarter, return No.
		-If the end_point is equal to origin, return Yes (we always start at origin no matter what the 
	command sequence is!)
		-else If the command sequence is a closed loop, new_start is at origin (0,0)
		-else:
			- Calculate the minimum number of full sequence repetitions before to get the 
			 the closes to the end point. (end / cmd.delta).
			- If the result is an integer >>> return Yes (new_start = repetition*cmd_delta)
			- else:
				new_start = cmd_delta*max(repetition - loopback, 0)
		- Start from new point then move through the sequence one step at a time and check if we 
		reached the end point, if not, return 'No'
	"""
    if end == Point(0, 0):
        log.debug('!!! End point is (0,0) !!!')
        return "Yes"

    elif cmd.is_loop:
        log.debug('Command sequence is a closed loop!')
        new_start_a = Point(0, 0)
        new_start_b = Point(0, 0)

    else:

        repeat = cmd.repeat_ratio(end)
        log.debug('Repeat point: %s', repeat)
        if repeat.x == 0:
            repeat = repeat.y
        elif repeat.y == 0:
            repeat = repeat.x
        else:
            repeat = min(repeat.x, repeat.y)

        log.debug('Repeat: %s', repeat)

        new_start_a = cmd.delta * max(int(repeat) - cmd.loopback_factor - 1, 0)
        new_start_b = cmd.delta * max(int(repeat) - cmd.loopback_factor, 0)

    log.info('New start A: %s', new_start_a)
    log.info('New start B: %s', new_start_b)

    log.debug('------\nWalking the robot:')
    for rep in range(cmd.loopback_factor + 1):
        for i in cmd.seq:
            log.debug('Current command: %s', i)
            if new_start_a == end or new_start_b == end:
                return "Yes"
            new_start_a += CMDSeq.trans[i]
            new_start_b += CMDSeq.trans[i]
            log.debug('Modified start A: %s.', new_start_a)
            log.debug('Modified start B: %s.', new_start_b)

    return "Yes" if (new_start_a == end) or (new_start_b == end) else "No"


def __starting_point():
    a = Robot()
    print(a)


__starting_point()

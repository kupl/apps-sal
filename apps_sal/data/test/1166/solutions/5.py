import sys
next(sys.stdin)
positions = {}
pos2x = {}
for (i, x) in enumerate(next(sys.stdin).split()):
    x = int(x)
    positions[x] = i
    pos2x[i] = x
answers = ['' for _ in range(len(positions))]
for x in range(len(positions), 0, -1):
    position = positions[x]

    def can_go_to_looser():
        next_position = position + x
        while next_position < len(positions):
            if pos2x[next_position] > x and answers[next_position] == 'B':
                return True
            next_position += x
        next_position = position - x
        while next_position >= 0:
            if pos2x[next_position] > x and answers[next_position] == 'B':
                return True
            next_position -= x
        return False
    if can_go_to_looser():
        answers[position] = 'A'
    else:
        answers[position] = 'B'
print(''.join(answers))

import sys
import collections


class GetOutOfLoop(Exception):
    pass


def __starting_point():

    n_cases = int(sys.stdin.readline())

    for case in range(n_cases):
        board = [list(sys.stdin.readline().rstrip()) for i in range(8)]
        knight_init_loc = [None, None]
        knight = 0
        for current_i in range(8):
            for current_j in range(8):
                if board[current_i][current_j] == 'K':
                    knight_init_loc[knight] = (current_i, current_j)
                    knight += 1

        to_explore = collections.deque()

        to_explore.append((knight_init_loc[0], 0))
        explored = set()
        try:
            while len(to_explore) > 0:
                ((current_i, current_j), current_step) = to_explore.popleft()
                explored.add((current_i, current_j))
                candidates = set()
                for inc_i in [-2, 2]:
                    for inc_j in [-2, 2]:
                        next_i, next_j = current_i + inc_i, current_j + inc_j
                        if 0 <= next_i < 8 and 0 <= next_j < 8 and (next_i, next_j) not in explored:
                            candidates.add(((next_i, next_j), current_step + 1))
                for (s, next_step) in candidates:
                    if s == knight_init_loc[1] and next_step % 2 == 0:
                        print('YES')
                        raise GetOutOfLoop
                    to_explore.append((s, next_step))
                current_step += 1
            print('NO')
        except GetOutOfLoop:
            pass
        sys.stdin.readline()


__starting_point()

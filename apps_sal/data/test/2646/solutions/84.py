import sys
from itertools import chain
YES = 'Yes'


def solve(N: int, M: int, A: 'List[int]', B: 'List[int]'):
    routes = [set() for _ in range(N)]
    marks = [None for _ in range(N)]
    for (a, b) in zip(A, B):
        a = a - 1
        b = b - 1
        routes[a].add(b)
        routes[b].add(a)
    marks[0] = -1
    cur_rooms = [0]
    count = 1
    while count < N:
        new_cur_rooms = []
        for cur_room in cur_rooms:
            next_rooms = list(routes[cur_room])
            for next_room in next_rooms:
                if marks[next_room] is None:
                    marks[next_room] = cur_room
                    new_cur_rooms.append(next_room)
                    count += 1
        cur_rooms = new_cur_rooms
    answer = 'Yes\n' + '\n'.join((str(n + 1) for n in marks[1:]))
    return answer


def main():
    tokens = chain(*(line.split() for line in sys.stdin))
    N = int(next(tokens))
    M = int(next(tokens))
    A = [int()] * M
    B = [int()] * M
    for i in range(M):
        A[i] = int(next(tokens))
        B[i] = int(next(tokens))
    answer = solve(N, M, A, B)
    print(answer)


def __starting_point():
    main()


__starting_point()

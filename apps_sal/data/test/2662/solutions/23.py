from collections import deque
from bisect import bisect_left


def main():
    N, *A = map(int, open(0))
    q = deque([])
    for i in range(N):
        d = bisect_left(q, A[i])
        if d == 0:
            q.appendleft(A[i])
        else:
            q[d - 1] = A[i]
    print(len(q))


def __starting_point():
    main()


__starting_point()

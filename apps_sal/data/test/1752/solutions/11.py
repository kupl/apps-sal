from collections import deque


def solve():
    N = int(input())
    A = [int(k) for k in input().split()]
    A.sort()
    results = deque([A[0]])
    front = 1
    for i in range(1, N):
        if front:
            results.appendleft(A[i])
        else:
            results.append(A[i])
        front ^= 1
    print(' '.join((str(k) for k in results)))


def __starting_point():
    solve()


__starting_point()

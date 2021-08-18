
import sys
from itertools import accumulate

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    N = int(readline())
    A = list(map(int, readline().split()))
    B = list(map(int, readline().split()))

    C = [0] * (N + 1)
    D = [0] * (N + 1)

    for i in range(N):
        C[A[i]] += 1
        D[B[i]] += 1

    for i in range(1, N + 1):
        if C[i] + D[i] > N:
            print('No')
            return

    print('Yes')

    C = list(accumulate(C))
    D = list(accumulate(D))

    B.reverse()

    i = 0
    while i < N and A[i] != B[i]:
        i += 1

    if i == N:
        print((*B))
        return

    n = A[i]

    idx_ng = []
    idx_ok = []

    for i in range(N):
        if A[i] == n and B[i] == n:
            idx_ng.append(i)
        elif A[i] != n and B[i] != n:
            idx_ok.append(i)

    for ng, ok in zip(idx_ng, idx_ok):
        B[ng], B[ok] = B[ok], B[ng]

    print((*B))
    return


def __starting_point():
    main()


__starting_point()

import sys
sys.setrecursionlimit(10**6)


def grun(A, K):
    if A < K:
        return 0
    a, b = divmod(A, K)
    if b == 0:
        return a
    a += 1
    r = A % a
    return grun((((a - 1) * K - r) // a) * a + r, K)


def solve():
    N = int(input())
    X = 0
    for _ in range(N):
        A, K = map(int, input().split())
        X ^= grun(A, K)
    print('Takahashi' if X else 'Aoki')


def __starting_point():
    solve()


__starting_point()

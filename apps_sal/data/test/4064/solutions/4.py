import sys

def solve():
    input = sys.stdin.readline
    N, H, L, R = map(int, input().split())
    A = [int(a) for a in input().split()]
    DP = [[-1] * H for _ in range(N)]
    DP[0][A[0]] = (1 if L <= A[0] <= R else 0)
    DP[0][A[0] - 1] = (1 if L <= A[0] - 1 <= R else 0)
    for i in range(1, N):
        for h in range(H):
            add = (1 if L <= h <= R else 0)
            if DP[i-1][(h - A[i]) % H] > -1: DP[i][h] = max(DP[i][h], DP[i-1][(h - A[i]) % H] + add)
            if DP[i-1][(h - A[i] + 1) % H] > -1: DP[i][h] = max(DP[i][h], DP[i-1][(h - A[i] + 1) % H] + add)
    print(max(DP[N-1]))
    return 0

def __starting_point():
    solve()
__starting_point()

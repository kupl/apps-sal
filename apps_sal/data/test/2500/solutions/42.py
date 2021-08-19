import sys
sys.setrecursionlimit(10 ** 9)
N = int(input())
mod = 10 ** 9 + 7
DP = dict()
DP[0, 0] = 1
DP[1, 0] = 1
DP[1, 1] = 2


def ans(S, X):
    if DP.get((S, X)) != None:
        return DP[S, X]
    if S == 0:
        return 1
    DP[S, X] = (ans(S // 2, X // 2) + ans((S - 1) // 2, (X - 1) // 2) + ans((S - 2) // 2, (X - 2) // 2)) % mod
    return DP[S, X]


print(ans(N, N))

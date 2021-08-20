import sys


def input():
    return sys.stdin.readline().strip()


def mapint():
    return map(int, input().split())


sys.setrecursionlimit(10 ** 9)
(N, M) = mapint()
As = list(mapint())
num_lis = [2, 5, 5, 4, 5, 6, 3, 7, 6]
need_m = [num_lis[a - 1] for a in As]
dp = [-1] * (N + 1)
dp[0] = 0
for i in range(1, N + 1):
    for (a, need) in zip(As, need_m):
        if need > i:
            continue
        elif dp[i - need] == -1:
            continue
        elif dp[i - need] == 0:
            dp[i] = max(dp[i], a)
        else:
            dp[i] = max(dp[i], dp[i - need] * 10 + a)
print(dp[-1])

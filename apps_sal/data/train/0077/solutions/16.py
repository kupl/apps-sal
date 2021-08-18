"""
NTC here
"""
from sys import setcheckinterval, stdin, setrecursionlimit
setcheckinterval(1000)
setrecursionlimit(10**7)


def iin(): return int(stdin.readline())


def lin(): return list(map(int, stdin.readline().split()))


for _ in range(iin()):
    n = iin()
    fence = [lin() for i in range(n)]
    dp = [[0, j, 2 * j] for i, j in fence]
    for i in range(1, n):
        for j in range(3):
            dp[i][j] += min([dp[i - 1][k] for k in range(3) if fence[i - 1][0] + k != fence[i][0] + j])
    print(min(dp[-1]))

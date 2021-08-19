import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline
n = int(input())
s = input()
a = list(map(int, input().split()))
N = len(a)
dp = [[[-1] * N for i in range(N)] for j in range(N)]


def calc(l, r, k):
    if dp[l][r][k] != -1:
        return dp[l][r][k]
    if l == r:
        return a[k]
    tmp = 0
    for i in range(l, r):
        tmp = max(tmp, calc(l, i, 0) + calc(i + 1, r, k))
        if s[i] == s[r]:
            tmp = max(tmp, calc(i + 1, r - 1, 0) + calc(l, i, k + 1))
    dp[l][r][k] = tmp
    return tmp


print(calc(0, n - 1, 0))

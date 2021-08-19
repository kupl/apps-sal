'''input
2 1 15
5 6
RG
'''
import math


def solve():
    n, s, k = map(int, input().split())
    s -= 1
    r = list(map(int, input().split()))
    c = input()
    inf = int(1e9)
    dp = [[inf for j in range(n)] for i in range(k + 1)]
    # dp[i][j] = minimum number of steps to get amount i if we start with jth index
    for i in range(0, k + 1):
        for j in range(0, n):
            if i == 0 or i <= r[j]:
                dp[i][j] = 0
                continue
            for K in range(0, n):
                if c[K] != c[j] and r[K] > r[j]:
                    dp[i][j] = min(dp[i][j], dp[i - r[j]][K] + int(abs(K - j)))
    ans = min(dp[k][i] + abs(i - s) for i in range(0, n))
    if ans >= inf:
        print(-1)
        return
    print(ans)
    return


t = 1
#t = int(input())
while t > 0:
    t -= 1
    solve()

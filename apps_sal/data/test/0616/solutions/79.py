import sys
import itertools

N,M = map(int, input().split())
AB = []
C = []
for _ in range(M):
    AB.append(tuple(map(int, input().split())))
    C.append(sum(1<<(int(x)-1) for x in map(int, input().split())))

INF = 10**18
dp = [INF]*(1<<N)
dp[0] = 0

for n,((a,b),c) in itertools.product(range(1<<N), zip(AB,C)):
    m = n|c
    x = dp[n] + a
    if dp[m] > x:
        dp[m] = x

ans = dp[-1]
if ans == INF:
    ans = -1
print(ans)

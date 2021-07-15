from math import gcd

n, X = map(int, input().split())
xlst = list(map(int, input().split()))
ans = X - xlst[0]
for x in xlst:
    ans = gcd(ans, X - x)
print(ans)

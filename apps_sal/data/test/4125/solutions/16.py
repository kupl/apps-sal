import math

n, x = map(int, input().split())
X = list(map(int, input().split()))

ans = []
for xx in X:
    ans.append(abs(x - xx))

a = ans[0]
for aa in ans:
    a = math.gcd(aa, a)

print(a)

import math
N, X = map(int, input().split())
lsx = list(map(int, input().split()))
lsx.sort()
gcd = abs(lsx[0] - X)
for i in range(1, N):
    gcd = math.gcd(gcd, lsx[i] - lsx[i - 1])
print(gcd)

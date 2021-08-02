import math
N, X = map(int, input().split())
xl = [abs(x - X)for x in map(int, input().split())]
ans = xl[0]

for x in xl[1:]:
    ans = math.gcd(ans, x)
print(ans)

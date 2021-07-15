import math

n, x = map(int, input().split())
xl = list(map(int, input().split()))

res = 0
for i in xl:
    res = math.gcd(res, abs(i-x))

print(res)

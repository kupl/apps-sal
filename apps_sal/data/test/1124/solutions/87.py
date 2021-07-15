import math
n = int(input())
res = 0
for ai in list(map(int, input().split())):
    res = math.gcd(res, ai)
print(res)

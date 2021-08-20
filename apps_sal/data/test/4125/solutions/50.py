import math
(n, x) = map(int, input().split())
num_list = list(map(int, input().split()))
res = 0
for i in num_list:
    res = math.gcd(res, abs(i - x))
print(res)

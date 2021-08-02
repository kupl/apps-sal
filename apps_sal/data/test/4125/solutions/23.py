import math
n, a = map(int, input().split())
x = list(map(int, input().split())) + [a]
x.sort()
if n == 1:
    print(abs(x[0] - x[1]))
    return
res = x[1] - x[0]
for i in range(1, n):
    res = math.gcd(res, x[i + 1] - x[i])
print(res)

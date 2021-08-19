from math import gcd
(n, x0) = list(map(int, input().split()))
x = [abs(_x - x0) for _x in list(map(int, input().split()))]
x.sort()
ans = x[0]
for i in range(n):
    ans = gcd(ans, x[i])
print(ans)

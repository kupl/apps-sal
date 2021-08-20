import math
(n, m) = map(int, input().split())
x = [int(x) for x in input().split()]
mi = min(x)
l = [abs(x[i] - x[i + 1]) for i in range(n - 1)]
ans = abs(mi - m)
for i in l:
    ans = math.gcd(ans, i)
print(ans)

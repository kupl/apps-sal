import math
(k, n, s, p) = map(int, input().split(' '))
ans = math.ceil(k * math.ceil(n / s) / p)
print(ans)

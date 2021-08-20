import math as m
(n, x, t) = map(int, input().split())
if n % x == 0:
    shong = int(n / x)
    ans = shong * t
    print(ans)
else:
    shong = m.floor(n / x)
    ans = (shong + 1) * t
    print(ans)

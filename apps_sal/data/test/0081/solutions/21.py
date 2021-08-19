from math import ceil


def gcd(a, b):
    while b:
        (a, b) = (b, a % b)
    return a


(a, b) = [int(item) for item in input().split()]
mn = float('inf')
ans = -1
d = abs(b - a)
if d == 0:
    print(0)
else:
    for g in range(1, int(d ** 0.5) + 1):
        if d % g != 0:
            continue
        k = min(ceil(b / g) * g - b, ceil(a / g) * g - a)
        if (a + k) % g == 0 and (b + k) % g == 0:
            if (a + k) * (b + k) // g < mn:
                mn = (a + k) * (b + k) // g
                ans = k
        g = d // g
        k = min(ceil(b / g) * g - b, ceil(a / g) * g - a)
        if (a + k) % g == 0 and (b + k) % g == 0:
            if (a + k) * (b + k) // g < mn:
                mn = (a + k) * (b + k) // g
                ans = k
    print(ans)

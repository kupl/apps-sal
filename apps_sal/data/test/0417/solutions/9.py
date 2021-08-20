from fractions import gcd
from itertools import accumulate


def solve(n, x, d):
    if d == 0:
        return 1 if x == 0 else n + 1
    elif d < 0:
        (x, d) = (-x, -d)
    g = gcd(x, d)
    x //= g
    d //= g
    lowers = [0] + list(accumulate(list(range(n))))
    uppers = [0] + list(accumulate(list(range(n - 1, -1, -1))))
    ans = 0
    for k_mod in range(min(n + 1, d)):
        k = k_mod
        offset = 0
        endpoints = []
        while k <= n:
            endpoints.append((lowers[k] + offset, 0))
            endpoints.append((uppers[k] + offset, 1))
            k += d
            offset += x
        endpoints.sort()
        opening = 0
        current_left = 0
        for (s, t) in endpoints:
            if t == 0:
                if opening == 0:
                    current_left = s
                opening += 1
            else:
                opening -= 1
                if opening == 0:
                    ans += s - current_left + 1
    return ans


(n, x, d) = list(map(int, input().split()))
print(solve(n, x, d))

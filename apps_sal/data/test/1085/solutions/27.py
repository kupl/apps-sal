def pf(x):
    plist = [1]
    p = 2
    while x > 1:
        t = 0
        while x % p == 0:
            x /= p
            t += 1
        now = list(plist)
        for i in range(t):
            now = list(map(lambda y: int(y * p), now))
            plist.extend(now)
        if p > int(x**0.5) + 1:
            p = x
        elif p == 2:
            p = 3
        else:
            p += 2
    return plist


N = int(input())
ans = len(pf(N - 1)) - 1
for x in pf(N)[1:]:
    M = N
    while M > 1 and M % x == 0:
        M //= x
    if M == 1 or M % x == 1:
        ans += 1
print(ans)

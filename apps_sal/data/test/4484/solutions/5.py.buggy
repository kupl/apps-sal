n, m = list(map(int, input().split()))

mod = 10**9 + 7
l = n + m
ans = 1
b = max(n, m)
s = min(n, m)
for i in range(l):
    if i % 2 == 0:
        tmp = b - i // 2
        if tmp > 0:
            ans = (ans % mod) * (tmp % mod)
        else:
            print((0))
            return
    else:
        tmp = s - i // 2
        if tmp > 0:
            ans = (ans % mod) * (tmp % mod)
        else:
            print((0))
            return
if l % 2 == 0:
    ans = (ans % mod) * (2 % mod)
print((ans % mod))

inf = 0x3f3f3f3f3f3f3f3f
M = mod = 1000000007
mod2inv = 500000004
pt = lambda *a, **k: print(*a, **k, flush=True)
rd = lambda: map(int, input().split())
n = int(input())
k = int(input())
a = int(input())
b = int(input())
r = 0
if k == 1:
    print((n - 1) * a)
    return
while n:
    if n % k:
        r += n % k * a
        n -= n % k
    r += min(b, (n - n // k) * a)
    n //= k
pt(r - a)

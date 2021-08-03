inf = int(1e9)
M = mod = 1000000007
mod2inv = 500000004
pt = lambda *a, **k: print(*a, **k, flush=True)
def rd(): return map(int, input().split())


n = int(input())
a = list(rd())
b = input()
l1 = -inf
l2 = inf
r1 = -inf
r2 = inf
f = 4
for i in range(4, n):
    x = b[i]
    if f == 4 and x == '1':
        l1 = max(l1, max(a[i - 4: i + 1]) + 1)
        f = 0
    if f == 4 and x == '0':
        l2 = min(l2, max(a[i - 4: i + 1]))
    if f == -4 and x == '1':
        r1 = max(r1, min(a[i - 4: i + 1]))
    if f == -4 and x == '0':
        r2 = min(r2, min(a[i - 4: i + 1]) - 1)
        f = 0
    if -4 < f < 4:
        if x == '0':
            f += 1
        if x == '1':
            f -= 1
print(min(l1, l2), max(r1, r2))

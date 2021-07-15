n, m = map(int, input().split())

l = -100
r = 100
for i in range(m):
    k, f = map(int, input().split())
    l = max(l, (k + f - 1) // f)
    if(f != 1):
        r = min(r, (k - 1) // (f - 1))

if(l == r):
    print((n + r - 1) // r)
elif ((n + r - 1) // r == (n + l - 1) // l):
    print((n + r - 1) // r)
else:
    print(-1)

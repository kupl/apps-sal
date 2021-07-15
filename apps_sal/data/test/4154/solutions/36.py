n, m = list(map(int, input().split()))
prel, prer = 0, 1e6
for i in range(m):
    l, r = list(map(int, input().split()))
    prel, prer = max(prel, l), min(prer, r)

if prer >= prel:
    print((prer - prel + 1))
else:
    print((0))


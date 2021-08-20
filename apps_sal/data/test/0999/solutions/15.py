n = int(input())
lc = 0
rc = 10 ** 9 + 1
for i in range(n):
    (l, r) = map(int, input().split())
    lc = max(l, lc)
    rc = min(r, rc)
m = int(input())
lp = 0
rp = 10 ** 9 + 1
for i in range(m):
    (l, r) = map(int, input().split())
    lp = max(l, lp)
    rp = min(r, rp)
print(max(0, lp - rc, lc - rp))

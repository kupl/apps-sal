n, w = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]
mx = 0
mn = 0
cur = 0
for aa in a:
    cur += aa
    mx = max(cur, mx)
    mn = min(cur, mn)

up = w - mx + 1
down = abs(mn)
if down > up:
    print(0)
else:
    print(up - down)

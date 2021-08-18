n = int(input())
m = int(input())
ns = []
for _ in range(n):
    ns.append(int(input()))
maxx = max(ns)
ans2 = maxx + m

hole = 0
for t in ns:
    hole += maxx - t

if hole >= m:
    ans1 = maxx
else:
    m -= hole
    ans1 = maxx + (m // n)
    if m % n != 0:
        ans1 += 1
print(ans1, ans2)

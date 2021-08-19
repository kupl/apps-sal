n = int(input())
interv = []
for i in range(n):
    (deb, fin) = list(map(int, input().split()))
    interv.append((deb, +1))
    interv.append((fin, -1))
interv.sort()
m = 0
y = 0
c = 0
for (t, dx) in interv:
    c += dx
    if c > m:
        m = c
        y = t
print(y, m)

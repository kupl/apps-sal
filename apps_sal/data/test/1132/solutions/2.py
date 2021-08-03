def R(): return map(int, input().split())


n, m = R()
c = [0] * n
for i in range(m):
    x, y = R()
    c[x - 1] += 1
    c[y - 1] += 1
c1 = c2 = 0
for i in range(n):
    if c[i] == 1:
        c1 += 1
    elif c[i] == 2:
        c2 += 1
if c2 == n:
    print("ring topology")
elif c1 == 2 and c2 == n - 2:
    print("bus topology")
elif c1 == n - 1:
    print("star topology")
else:
    print("unknown topology")

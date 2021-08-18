n, m = [int(x) for x in str(input()).split(' ', 1)]
a = []
b = []
d = []
for _ in range(n):
    lx, rx = [int(x) for x in str(input()).split(' ', 1)]
    a.append(lx)
    b.append(rx)
    d.append(lx - rx)
if sum(b) > m:
    print(-1)
    return
if sum(a) <= m:
    print(0)
    return
s = sum(a)
for i, v in enumerate(sorted(d, reverse=True)):
    s -= v
    if s <= m:
        print(i + 1)
        break

n, x, m = map(int, input().split())
if m >= n:
    ans = 0
    for i in range(n):
        ans += x
        x **= 2
        x %= m
    print(ans)
    return
l = [x]
d = {}
for i in range(m):
    d[i] = 0
d[x] += 1
for i in range(m):
    x = (x**2) % m
    if d[x] == 1:
        y = l.index(x)
        print(sum(l[:y]) + sum(l[y:]) * ((n - y) // (len(l) - y)) + sum(l[y:][:(n - y) % (len(l) - y)]))
        return
    l.append(x)
    d[x] += 1

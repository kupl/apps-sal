q, w = list(map(int, input().split()))
z, x, c, v = -1, -1, -1, -1
a = []
s = 0
for i in range(0, q):
    e = input()
    if e.count('B') != 0:
        s += e.count('B')
        n = e.find('B')
        m = e.rfind('B')
        if c == -1:
            c = i
        v = i
        if z == -1:
            z = n
        else:
            z = min(z, n)
        x = max(x, m)
    a.append(e)
z, x = x - z + 1, v - c + 1
if max(z, x) > min(q, w):
    print(-1)
elif x * z == 0:
    print(1)
else:
    print(max(z, x)**2 - s)

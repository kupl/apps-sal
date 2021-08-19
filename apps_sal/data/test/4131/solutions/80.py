(n, m) = list(map(int, input().split()))
c = [0] * (n + 1)
py = []
for i in range(m):
    py.append(list(map(int, input().split())) + [i])
py.sort(key=lambda x: x[1])
a = [''] * m
for (p, y, i) in py:
    c[p] += 1
    x = c[p]
    z = str(p * 1000000 + x)
    if len(z) < 12:
        a[i] = '0' * (12 - len(z)) + z
    else:
        a[i] = z
for x in a:
    print(x)

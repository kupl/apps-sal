v = input().strip().split(',')
v = [(v[i * 2], int(v[i * 2 + 1])) for i in range(len(v) // 2)]
n = len(v)

f = {}
s = [1000000]
for i in range(n):
    x, m = v[i]
    d = len(s)
    if d not in f:
        f[d] = []
    f[d].append(x)
    s.append(m)
    while s[-1] <= 0:
        s.pop()
        s[-1] -= 1

r = sorted([(k, v) for k, v in list(f.items())])
print(len(r))
for i in range(len(r)):
    print(' '.join(r[i][1]))

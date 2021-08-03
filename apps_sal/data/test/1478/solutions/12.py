t = input().split(',')
k, m = 0, len(t)
p, d = [m] * m, [[] for i in range(m)]
for s, n in zip(t[::2], t[1::2]):
    while not p[k]:
        k -= 1
    p[k] -= 1
    d[k].append(s)
    k += 1
    p[k] = int(n)
while d[k]:
    k += 1
print(k)
for q in d[:k]:
    print(*q)

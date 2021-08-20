t = input().split(',')
m = len(t)
(p, d, k) = ([m] * m, [[] for i in range(m)], 0)
for i in range(0, m, 2):
    (s, n) = (t[i], int(t[i + 1]))
    while p[k] == 0:
        k -= 1
    p[k] -= 1
    d[k].append(s)
    k += 1
    p[k] = n
while d[k]:
    k += 1
print(k)
for q in d[:k]:
    print(*q)

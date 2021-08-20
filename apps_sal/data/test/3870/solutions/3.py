(n, m) = map(int, input().split())
(a, d) = ([1000000000.0], [1000000000.0])
for x in range(n):
    (p, s) = input().split()
    [d, a][p < 'B'].append(int(s))
v = [int(input()) for y in range(m)]
for q in [a, d, v]:
    q.sort()
s = sum(v)
i = j = 0
for t in v:
    if t > d[i]:
        (s, i) = (s - t, i + 1)
    elif t >= a[j]:
        (s, j) = (s - a[j], j + 1)
if i + j - n:
    s = 0
print(max(s, sum((max(0, y - x) for (x, y) in zip(a, v[::-1])))))

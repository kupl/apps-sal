((h, w, m), *e) = [[*map(int, i.split())] for i in open(0)]
(a, b) = ([0] * h, [0] * w)
for (y, x) in e:
    a[y - 1] += 1
    b[x - 1] += 1
ans = max(a) + max(b)
c = a.count(max(a)) * b.count(max(b)) - sum((a[y - 1] + b[x - 1] == ans for (y, x) in e))
print(ans - (c <= 0))

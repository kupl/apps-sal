n, m, c = map(int, input().split())
b = list(map(int, input().split()))
d = 0
for i in range(n):
    a = list(map(int, input().split()))
    e = []
    for j in range(m):
        e.append(a[j] * b[j])
    e.append(c)
    if sum(e) > 0:
        d += 1
print(d)

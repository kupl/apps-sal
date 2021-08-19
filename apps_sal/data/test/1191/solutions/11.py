(n, k) = list(map(int, input().split()))
a = list(map(int, input().split()))
s = list(map(int, input().split()))
for q in range(n):
    a[q] = [a[q], s[q], q]
a.sort()
(b, d, z) = ([0] * k, 0, [[] for q in range(n)])
for q in range(n):
    z[a[q][2]] = d + a[q][1]
    (l, j) = (0, 0)
    for q1 in range(k):
        if l == 1:
            (b[q1], j) = (j, b[q1])
        elif a[q][1] > b[q1]:
            (l, j) = (1, b[q1])
            d += a[q][1] - b[-1]
            b[q1] = a[q][1]
print(*z)

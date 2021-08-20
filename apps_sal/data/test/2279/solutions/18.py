n = int(input())
a = []
b = [0] * (2 * n + 1)
c = [0] * (2 * n + 1)
z = dict()
for i in range(2 * n - 1):
    k = list(map(int, input().split()))
    for j in range(len(k)):
        z[k[j]] = (i + 2, j + 1)
    a += k
a.sort(reverse=True)
for d in range(len(a)):
    (i, j) = z[a[d]]
    if not c[i] and (not c[j]):
        b[i] = j
        b[j] = i
        c[i] = c[j] = True
for i in range(1, 2 * n + 1):
    print(b[i], end=' ')

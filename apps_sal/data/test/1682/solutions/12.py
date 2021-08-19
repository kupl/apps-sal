(n, k) = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list()
for i in range(n):
    c.append((i, b[i] - a[i]))
c.sort(key=lambda x: x[1])
c = c[::-1]
r = 0
for i in range(n):
    if i < k or c[i][1] > 0:
        r += a[c[i][0]]
    else:
        r += b[c[i][0]]
print(r)

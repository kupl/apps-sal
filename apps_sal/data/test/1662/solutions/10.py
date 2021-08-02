n = int(input())
a = list(map(int, input().split()))
a.sort()
last = 0
v = [0] * n
b = []
for i in range(n):
    if a[i] > last:
        last = a[i]
        b.append(a[i])
        v[i] = 1
for i in range(n - 1, -1, -1):
    if not v[i] and a[i] < last:
        last = a[i]
        b.append(a[i])
        v[i] = 1
tmp = len(b)
print(tmp)
for i in range(tmp):
    print(b[i], end=' ')

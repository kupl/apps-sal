n = int(input())
a = [0]
for i in range(n):
    a.append(int(input()))
a.append(0)
l = [0] * (n + 2)
l[0] = 0
for i in range(1, n + 1):
    l[i] = max(l[i - 1], a[i])
r = [0] * (n + 2)
r[n] = 0
for i in range(n, 0, -1):
    r[i] = max(r[i + 1], a[i])
for i in range(1, n + 1):
    print(max(l[i - 1], r[i + 1]))

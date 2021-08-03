n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = [0] * n
d = [0] * n
g = 0
for i in range(n):
    c[a[i] - 1] += 1
    d[b[i] - 1] += 1
for i in range(n):
    g = max(g, c[i] + d[i])
e = [c[0]]
f = [d[0]]
h = e[0]
for i in range(1, n):
    e.append(c[i] + e[-1])
    f.append(d[i] + f[-1])
for i in range(n - 1):
    h = max(h, e[i + 1] - f[i])
if g > n:
    print("No")
else:
    print("Yes")
    print(*(b[n - h:] + b[:n - h]))

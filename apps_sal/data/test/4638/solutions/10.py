(n, c) = map(int, input().split())
a = [0] + [int(i) for i in input().split()]
b = [0] + [int(i) for i in input().split()]
p = [0] * n
l = [0] * n
t = [0] * n
for i in range(1, n):
    p[i] = a[i] + t[i - 1]
    l[i] = b[i] + t[i - 1] - (c if t[i - 1] == l[i - 1] + c else 0)
    l[i] = min(l[i], l[i - 1] + b[i])
    t[i] = min(l[i] + c, p[i])
for i in t:
    print(i, end=' ')

n = int(input())
v = list(map(int, input().split()))
a = [0 for i in range(n)]
a[0] = v[0]
for i in range(1, n):
    a[i] = a[i - 1] + v[i]
a += [0]
v = sorted(v)
b = [0 for i in range(n)]
b[0] = v[0]
for i in range(1, n):
    b[i] = b[i - 1] + v[i]
b += [0]
m = int(input())
for i in range(m):
    t, l, r = list(map(int, input().split()))
    if t - 1:
        print(b[r - 1] - b[l - 2])
    else:
        print(a[r - 1] - a[l - 2])

(n, m) = list(map(int, input().split()))
b = list(map(int, input().split()))
a = [0] * (n + 1)
minb = n + 1
for x in b:
    if x < minb:
        minb = x
        a[x] = x
v = a[1]
for i in range(2, n + 1):
    if a[i] == 0:
        a[i] = v
    else:
        v = a[i]
print(' '.join(map(str, a[1:])))

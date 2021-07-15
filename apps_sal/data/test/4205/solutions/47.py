n = int(input())
a = list(map(int, input().split(' ')))

ok = 0
f = 1
for i in range(n):
    if a[i] - 1 != i:
        f = 0
if f:
    ok = 1
for i in range(n):
    for j in range(i + 1, n):
        a[i], a[j] = a[j], a[i]
        f = 1
        for k in range(n):
            if a[k] - 1 != k:
                f = 0
        if f:
            ok = 1
        a[i], a[j] = a[j], a[i]
print('YES' if ok else 'NO')

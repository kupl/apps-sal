n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
kek = 1000000000000000000
for i in range(n):
    l = 0
    ti = -1000000000000000000
    for j in range(n):
        if j == i:
            continue
        for k in range(m):
            ti = max(a[j] * b[k], ti)
    kek = min(kek, ti)
print(kek)

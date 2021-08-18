from copy import copy
n, *x = list(map(int, open(0).read().split()))
a = []
for i, v in enumerate(x):
    a.append((v, i))
a.sort()

ans = [0] * n
for i in range(n):
    if i <= (n - 1) // 2:
        ans[a[i][1]] = a[n // 2][0]
    else:
        ans[a[i][1]] = a[(n - 1) // 2][0]
for y in ans:
    print(y)

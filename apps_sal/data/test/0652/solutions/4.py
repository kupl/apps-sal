from collections import defaultdict
n = int(input())
x = []
y = []
for i in range(n):
    x.append(0)
    y.append(0)
    (x[i], y[i]) = list(map(int, input().split()))
dict = defaultdict(int)
for i in range(n):
    for j in range(i + 1, n):
        tx = x[i] - x[j]
        ty = y[i] - y[j]
        if tx > 0 or (tx == 0 and ty > 0):
            tx = -tx
            ty = -ty
        dict[tx, ty] += 1
ans = 0
for i in list(dict.values()):
    ans += i * (i - 1) // 2
print(ans // 2)

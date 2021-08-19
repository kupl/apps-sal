Q = int(input())
lim = 10 ** 5 + 10
p = [True] * lim
p[0] = False
p[1] = False
for i in range(2, int(lim ** 0.5) + 1):
    for j in range(i * 2, 10 ** 5 + 1, i):
        p[j] = False
y = [0] * lim
for i in range(3, lim, 2):
    y[i] = y[i - 2]
    if p[i] and p[(i + 1) // 2]:
        y[i] += 1
    y[i - 1] = y[i - 2]
for _ in range(Q):
    (l, r) = map(int, input().split())
    print(y[r] - y[l - 1])

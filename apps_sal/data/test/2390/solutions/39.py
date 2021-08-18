
n, c = list(map(int, input().split()))

x, v = [], []
for i in range(n):
    a, b = list(map(int, input().split()))
    x.append(a)
    v.append(b)

cw = [0] * (n + 1)
ccw = [0] * (n + 1)
for i in range(n):
    cw[i + 1] = cw[i] + v[i]
    ccw[i + 1] = ccw[i] + v[-i - 1]


for i in range(1, n + 1):
    cw[i] -= x[i - 1]
    ccw[i] -= c - x[-i]


maxcw = [0] * (n + 1)
maxccw = [0] * (n + 1)
for i in range(1, n + 1):
    maxcw[i] = max(maxcw[i - 1], cw[i])
    maxccw[i] = max(maxccw[i - 1], ccw[i])

ans = max(0, maxcw[-1], maxccw[-1])

for i in range(1, n + 1):
    ans = max(ans, cw[i] + maxccw[-i - 1] - x[i - 1])
    ans = max(ans, ccw[i] + maxcw[-i - 1] - (c - x[-i]))

print(ans)

N = int(input())
lm = [float('INF')] * 3
rm = [-float('INF')] * 3
um = [-float('INF')] * 3
dm = [float('INF')] * 3
for i in range(N):
    (x, y, d) = input().split()
    x = int(x)
    y = int(y)
    if d == 'L':
        um[1] = max(um[1], y)
        dm[1] = min(dm[1], y)
        lm[2] = min(lm[2], x)
        rm[0] = max(rm[0], x)
    if d == 'R':
        um[1] = max(um[1], y)
        dm[1] = min(dm[1], y)
        lm[0] = min(lm[0], x)
        rm[2] = max(rm[2], x)
    if d == 'U':
        um[2] = max(um[2], y)
        dm[0] = min(dm[0], y)
        lm[1] = min(lm[1], x)
        rm[1] = max(rm[1], x)
    if d == 'D':
        um[0] = max(um[0], y)
        dm[2] = min(dm[2], y)
        lm[1] = min(lm[1], x)
        rm[1] = max(rm[1], x)
time = [0]


def calc(t):
    x = max(rm[1], rm[0] - t, rm[2] + t) - min(lm[1], lm[0] + t, lm[2] - t)
    y = max(um[1], um[0] - t, um[2] + t) - min(dm[1], dm[0] + t, dm[2] - t)
    return x * y


for i in range(3):
    for j in range(i):
        t = (lm[i] - lm[j]) / (i - j)
        if t > 0:
            time.append(t)
        t = (dm[i] - dm[j]) / (i - j)
        if t > 0:
            time.append(t)
        t = (rm[j] - rm[i]) / (i - j)
        if t > 0:
            time.append(t)
        t = (um[j] - um[i]) / (i - j)
        if t > 0:
            time.append(t)
ans = float('INF')
for t in time:
    ans = min(ans, calc(t))
print(ans)

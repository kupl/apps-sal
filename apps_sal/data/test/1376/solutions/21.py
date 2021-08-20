n = int(input())
a = [int(x) for x in input().split()]
f = {}
for (i, x) in enumerate(a):
    if x not in f:
        f[x] = [i]
    else:
        f[x].append(i)
        f[x].sort()
l = 0
cnt = 0
r = 0
for i in range(1, n + 1):
    if abs(f[i][0] - l) + abs(f[i][1] - r) < abs(f[i][1] - l) + abs(f[i][0] - r):
        cnt += abs(f[i][0] - l)
        l = f[i][0]
        cnt += abs(f[i][1] - r)
        r = f[i][1]
    else:
        cnt += abs(f[i][1] - l)
        l = f[i][1]
        cnt += abs(f[i][0] - r)
        r = f[i][0]
print(cnt)

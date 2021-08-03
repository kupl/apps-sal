s = input()
n = len(s)
f = [[0 for i in range(0, 3)] for j in range(0, n)]
for i in range(0, n):
    if (i > 0):
        f[i][0] = f[i - 1][0]
        f[i][1] = f[i - 1][1]
        f[i][2] = f[i - 1][2]
    if (s[i] == 'a'):
        f[i][0] += 1
        f[i][2] += 1
        f[i][2] = max(f[i][2], f[i][1] + 1)
    else:
        f[i][1] += 1
        f[i][1] = max(f[i][1], f[i][0] + 1)
print(max(f[n - 1][0], max(f[n - 1][1], f[n - 1][2])))

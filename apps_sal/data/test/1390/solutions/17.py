(n, m) = list(map(int, input().split()))
f = list(map(int, input().split()))
f.sort()
lpd = f[n - 1] - f[0]
for i in range(1, m - n + 1, 1):
    if f[i + n - 1] - f[i] < lpd:
        lpd = f[i + n - 1] - f[i]
print(lpd)

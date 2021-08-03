n = int(input()) - 1
a = sorted(list(map(int, input().split())))
k = a[-1]
kk = k // 2
x, b = 10**9, 10**9
for i in range(n):
    if abs(a[i] - kk) <= x:
        x = abs(a[i] - kk)
        b = a[i]
print(k, b)

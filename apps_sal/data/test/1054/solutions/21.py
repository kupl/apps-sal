n = int(input())
xl, yl = list(map(int, input().split()))
xr, yr = list(map(int, input().split()))
if xl > xr:
    xl, xr = xr, xl
if yl > yr:
    yl, yr = yr, yl
for i in range(n - 2):
    x, y = list(map(int, input().split()))
    xl = min(xl, x)
    xr = max(xr, x)
    yl = min(yl, y)
    yr = max(yr, y)
print(max(yr - yl, xr - xl)**2)

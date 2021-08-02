w, h, n = map(int, input().split())

xl, xr = 0, w
yl, yu = 0, h
for i in range(n):
    x, y, a = map(int, input().split())
    if a == 1:
        xl = max(xl, x)
    elif a == 2:
        xr = min(xr, x)
    elif a == 3:
        yl = max(yl, y)
    else:
        yu = min(yu, y)

print((xr - xl) * (yu - yl)) if xl < xr and yl < yu else print(0)

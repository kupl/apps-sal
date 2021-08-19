(a, b, x_yoko, y_tate) = list(map(int, input().split()))
if a == b:
    ans = x_yoko
elif a > b:
    up = (a - b) * 2 * x_yoko - x_yoko
    cross = (a - b - 1) * y_tate + x_yoko
    ans = min(up, cross)
else:
    up = (b - a) * y_tate + x_yoko
    cross = (b - a) * 2 * x_yoko + x_yoko
    ans = min(up, cross)
print(ans)


xs, ys = list(map(int, input().split()))
xf, yf = list(map(int, input().split()))

if xs == xf:
    print((abs(yf - ys) + 1) * 2 + 4)
    return
elif ys == yf:
    print((abs(xf - xs) + 1) * 2 + 4)
    return

xs, xf = sorted([xs, xf])
ys, yf = sorted([ys, yf])

xf += 1
yf += 1

print(2 * (xf - xs) + 2 * (yf - ys))


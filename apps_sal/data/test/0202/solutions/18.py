(xi, yi) = map(int, input().split())
(xf, yf) = map(int, input().split())
xf = abs(xf - xi)
yf = abs(yf - yi)
steps = 0
if xf == yf:
    steps += xf
elif xf == 0:
    steps += yf
elif yf == 0:
    steps += xf
else:
    reduce = min(xf, yf)
    steps += reduce
    steps += max(xf, yf) - reduce
print(steps)

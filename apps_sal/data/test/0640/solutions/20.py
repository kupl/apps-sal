a, b = map(int, input().split())
c, d, e = 0, 0, 0
for i in range(1, 7):
    if abs(i - a) < abs(i - b):
        c += 1
    elif abs(i - a) > abs(i - b):
        e += 1
    else:
        d += 1
print(c, d, e, sep=' ')

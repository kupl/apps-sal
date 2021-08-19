n = int(input())
s = 0.0
for i in range(0, n):
    data = input().split()
    (x, y) = (float(data[0]), float(data[1]))
    s += y
print('%.3f' % (5 + s / n))

x = [0] * 4
y = [0] * 4

x[0], y[0], x[1], y[1] = map(int, input().split())

xdist = x[1] - x[0]
ydist = y[1] - y[0]

x[2] = x[1] - ydist
y[2] = y[1] + xdist

x[3] = x[2] - xdist
y[3] = y[2] - ydist

print(x[2], y[2], x[3], y[3])

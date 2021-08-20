def sLayer(n):
    return 3 * n * (n + 1)


def getLayer(N):
    a = 0
    b = 600000000
    while b - a > 1:
        n = (a + b) // 2
        tN = sLayer(n)
        if tN > N:
            b = n
        else:
            a = n
    return a


N = int(input())
if N == 0:
    print('0 0')
    raise SystemExit
N -= 1
layer = getLayer(N)
N -= sLayer(layer)
seg = N // (layer + 1)
idx = N % (layer + 1)
segDiff = [(-1, 2), (-2, 0), (-1, -2), (1, -2), (2, 0), (1, 2)]
if seg == 0:
    x = 2 * layer + 1
    y = 2
elif seg == 1:
    x = -1 + layer
    y = 2 * (layer + 1)
elif seg == 2:
    x = -2 - layer
    y = 2 * layer
elif seg == 3:
    x = -1 - 2 * layer
    y = -2
elif seg == 4:
    x = 1 - layer
    y = -2 - 2 * layer
elif seg == 5:
    x = 2 + layer
    y = -2 * layer
x += segDiff[seg][0] * idx
y += segDiff[seg][1] * idx
print('%d %d' % (x, y))

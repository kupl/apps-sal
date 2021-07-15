from cmath import phase

N, *XY = map(int, open(0).read().split())

XY = sorted((complex(x, y) for x, y in zip(*[iter(XY)] * 2)), key=phase)
XY += XY

print(max(abs(sum(XY[i:j])) for i in range(2 * N + 1) for j in range(2 * N + 1) if j - i <= N))

n, l, r = map(int, input().split())
sm = 0
for i in range(l):
    sm += 2 ** i
print(sm + n - l, end=' ')
sm = 0
for i in range(r):
    sm += 2 ** i
sm += 2 ** (r - 1) * (n - r)
print(sm)

(n, m, k) = list(map(int, input().split()))
d = {}
if m > 0:
    for x in map(int, input().split()):
        d[x] = True
ball = 1
for i in range(k):
    if ball in d:
        break
    (x, y) = list(map(int, input().split()))
    ball = x if ball == y else y if ball == x else ball
print(ball)

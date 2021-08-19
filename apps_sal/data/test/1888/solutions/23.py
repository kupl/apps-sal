(n, m) = map(int, input().split())
baaki = [0] * 15000
for i in range(m):
    (x, y, cbaaki) = map(int, input().split())
    baaki[x] += cbaaki
    baaki[y] -= cbaaki
sm = 0
for i in baaki:
    if i > 0:
        sm += i
print(sm)

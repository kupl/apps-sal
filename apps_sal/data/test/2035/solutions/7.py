import sys
(n, sx, sy) = list(map(int, sys.stdin.readline().strip().split()))
(a, b, c, d) = (0, 0, 0, 0)
for i in range(n):
    (x, y) = list(map(int, sys.stdin.readline().strip().split()))
    if x < sx:
        a += 1
    if x > sx:
        b += 1
    if y > sy:
        c += 1
    if y < sy:
        d += 1
z = max(a, b, c, d)
print(z)
if a == z:
    print(sx - 1, sy)
elif b == z:
    print(sx + 1, sy)
elif c == z:
    print(sx, sy + 1)
else:
    print(sx, sy - 1)

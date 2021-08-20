import sys
readline = sys.stdin.readline


def mhd(A, B):
    return abs(A[0] - B[0]) + abs(A[1] - B[1])


(x0, y0, ax, ay, bx, by) = map(int, readline().split())
(xs, ys, T) = map(int, readline().split())
Points = [(x0, y0)]
for _ in range(100):
    (xp, yp) = Points[-1]
    Points.append((xp * ax + bx, yp * ay + by))
ans = 0
pre = (xs, ys)
for st in range(100):
    L = mhd(pre, Points[st])
    if L > T:
        continue
    res = 1
    for j in range(st + 1, 100):
        L += mhd(Points[j - 1], Points[j])
        if L > T:
            break
        res += 1
    ans = max(ans, res)
    res = 1
    L = mhd(pre, Points[st])
    for j in range(st - 1, -1, -1):
        L += mhd(Points[j + 1], Points[j])
        if L > T:
            break
        res += 1
    ans = max(ans, res)
print(ans)

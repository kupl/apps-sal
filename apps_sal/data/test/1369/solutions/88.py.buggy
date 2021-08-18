def circum(A, B, C):
    # 三角形ABCの外心
    Ax, Ay = A
    Bx, By = B
    Cx, Cy = C
    a = (Bx - Cx)**2 + (By - Cy)**2
    b = (Cx - Ax)**2 + (Cy - Ay)**2
    c = (Ax - Bx)**2 + (Ay - By)**2
    s = a * (b + c - a)
    t = b * (c + a - b)
    u = c * (a + b - c)
    Ux = (s * Ax + t * Bx + u * Cx) / (s + t + u)
    Uy = (s * Ay + t * By + u * Cy) / (s + t + u)
    return Ux, Uy


def dist2(a, b):
    # 2点a,bの距離の2乗
    ax, ay = a
    bx, by = b
    return (ax - bx)**2 + (ay - by)**2


n = int(input())
P = [tuple(map(int, input().split())) for i in range(n)]
eps = 10**(-7)
if n == 2:
    r = dist2(P[0], P[1])**0.5 / 2
    print(r)
    return
for i in range(n - 2):
    for j in range(i + 1, n - 1):
        for k in range(j + 1, n):
            a, b, c = P[i], P[j], P[k]
            ax, ay = a
            bx, by = b
            cx, cy = c
            if dist2(a, b) + dist2(b, c) <= dist2(c, a):
                p = (cx + ax) / 2, (cy + ay) / 2
                r2 = dist2(a, p)
            elif dist2(b, c) + dist2(c, a) <= dist2(a, b):
                p = (ax + bx) / 2, (ay + by) / 2
                r2 = dist2(b, p)
            elif dist2(c, a) + dist2(a, b) <= dist2(b, c):
                p = (bx + cx) / 2, (by + cy) / 2
                r2 = dist2(c, p)
            else:
                p = circum(a, b, c)
                r2 = dist2(a, p)
            if all([dist2(p, q) <= r2 + eps for q in P]):
                print((r2**0.5))
                return

N = int(input())
A = []
for i in range(N):
    x, y = list(map(int, input().split()))
    A.append((x, y))


def c(P1, P2, P3):
    x1, y1 = P1
    x2, y2 = P2
    x3, y3 = P3
    a = 2 * (x1 - x2)
    b = 2 * (y1 - y2)
    p = x1**2 - x2**2 + y1**2 - y2**2
    c = 2 * (x1 - x3)
    d = 2 * (y1 - y3)
    q = x1**2 - x3**2 + y1**2 - y3**2
    det = a * d - b * c
    x = d * p - b * q
    y = a * q - c * p
    if det < 0:
        x = -x
        y = -y
        det = -det
    if det != 0:
        x /= det
        y /= det
    r = ((x - x1)**2 + (y - y1)**2)**0.5
    return x, y, r


ans = (200000)**2
for i in range(N - 1):
    for j in range(i + 1, N):
        f = 0
        x1, y1 = A[i][0], A[i][1]
        x2, y2 = A[j][0], A[j][1]
        x, y = (x1 + x2) / 2, (y1 + y2) / 2
        r = ((x1 - x)**2 + (y1 - y)**2)**0.5
        for a, b in A:
            d = ((a - x)**2 + (b - y)**2)**0.5
            if d > r:
                f = 1
                break
        if f == 0:
            ans = min(ans, r)
f = 0

if N > 2:
    for i in range(N - 2):
        for j in range(i + 1, N - 1):
            for k in range(j + 1, N):
                f = 0
                x, y, r = c(A[i], A[j], A[k])
                for a, b in A:
                    d = ((a - x)**2 + (b - y)**2)**0.5
                    if d > r:
                        f = 1
                        break
                if f == 0:
                    ans = min(ans, r)
print(ans)

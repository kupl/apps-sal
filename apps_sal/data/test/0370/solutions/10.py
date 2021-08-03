K = int(input())
X, Y = list(map(int, input().split()))

P = []
x, y = 0, 0

while (x, y) != (X, Y):
    dx = abs(X - x)
    dy = abs(Y - y)
    D = dx + dy
    if D == K:
        x, y = X, Y
    elif D % 2 != 0 and K % 2 == 0:
        print((-1))
        return
    elif D % 2 == 0 and D <= 2 * K:
        pos = D // 2
        shift = (2 * K - D) // 2
        if pos <= dx:
            x += pos if X > x else -pos
            y -= shift if Y > y else -shift
        else:
            x = X + (shift if X > x else -shift)
            y += pos - dx if Y > y else -(pos - dx)
    elif D < K:
        x -= K if X > x else -K
    elif dx >= K:
        x += K if X > x else -K
    else:
        x = X
        y += K - dx if Y > y else -(K - dx)
    P.append((x, y))

print((len(P)))
for x, y in P:
    print((x, y))

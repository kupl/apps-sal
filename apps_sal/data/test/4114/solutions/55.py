def dist(a, b, x, y, h):
    return h + abs(a - x) + abs(b - y)


N = int(input())
P = []
for i in range(N):
    x, y, h = map(int, input().split())
    P.append([h, x, y])
P.sort(reverse=True)

for i in range(101):
    for j in range(101):
        H = dist(i, j, P[0][1], P[0][2], P[0][0])
        for p in P[1:]:
            if max(H - abs(p[1] - i) - abs(p[2] - j), 0) != p[0]:
                break
        else:
            print(i, j, H)
            break

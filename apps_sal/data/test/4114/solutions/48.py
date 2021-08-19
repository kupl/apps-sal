def dist(h, xi, yi, cx, cy):
    return h + abs(xi - cx) + abs(yi - cy)


N = int(input())
P = []
for i in range(N):
    (xi, yi, h) = map(int, input().split())
    P.append([h, xi, yi])
P.sort(reverse=True)
for i in range(101):
    for j in range(101):
        H = dist(P[0][0], P[0][1], P[0][2], i, j)
        for p in P[1:]:
            if max(H - abs(p[1] - i) - abs(p[2] - j), 0) != p[0]:
                break
        else:
            print(i, j, H)
            break

N = int(input())
P = [list(map(int, input().split())) for n in range(N)]
(x, y, h) = list(filter(lambda x: x[2], P))[0]
for i in range(101):
    for j in range(101):
        H = h + abs(x - i) + abs(y - j)
        if all((max(H - abs(t[0] - i) - abs(t[1] - j), 0) == t[2] for t in P)):
            print(i, j, H)

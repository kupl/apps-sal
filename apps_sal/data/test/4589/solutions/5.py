H, W = map(int, input().split())
S = []
for i in range(H):
    S.append(list(input()))
for j in range(H):
    for p in range(W):
        if S[j][p] == ".":
            c = 0
            for h, w in [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, -1), (-1, 1), (1, -1)]:
                if 0 <= j + h <= H - 1 and 0 <= p + w <= W - 1 and S[j + h][p + w] == "
                c += 1
                S[j][p] = c
for i in S:
    print(*i, sep="")

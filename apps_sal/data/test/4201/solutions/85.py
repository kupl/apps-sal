(H, W, K) = map(int, input().split())
C = []
for _ in range(H):
    C.append(list(input()))
ans = 0
for bith in range(1 << H):
    for bitw in range(1 << W):
        black = 0
        for h in range(H):
            for w in range(W):
                if C[h][w] == '#' and bith & 1 << h and bitw & 1 << w:
                    black += 1
        if black == K:
            ans += 1
print(ans)

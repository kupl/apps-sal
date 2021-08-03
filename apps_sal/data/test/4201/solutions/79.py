H, W, K = [int(v) for v in input().split()]
G = []
for _ in range(H):
    G.append(input())

ans = 0

for mask_r in range(1 << H):
    for mask_c in range(1 << W):
        black = 0
        for i in range(H):
            for j in range(W):
                if ((mask_r >> i) & 1 == 0) and ((mask_c >> j) & 1 == 0) and G[i][j] == "#":
                    black += 1
        if black == K:
            ans += 1

print(ans)

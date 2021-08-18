
H, W, K = list(map(int, input().split()))

G = []
for _ in range(H):
    G.append(input())

ans = 0

black = 0

for mask_h in range(1 << H):
    for mask_w in range(1 << W):
        black = 0
        for i in range(H):
            for j in range(W):
                if((mask_h >> i) & 1 == 0) and ((mask_w >> j) & 1 == 0) and G[i][j] == '
                black += 1
        if black == K:
            ans += 1

print(ans)

H, W, K = list(map(int, input().split()))
c = [input() for _ in range(H)]

ans = 0
for i in range(1 << H):
    for j in range(1 << W):
        cnt = 0
        for h in range(H):
            for w in range(W):
                if c[h][w] == '
                if (i >> h) % 2 == 0 and (j >> w) % 2 == 0:
                    cnt += 1
        if cnt == K:
            ans += 1
print(ans)

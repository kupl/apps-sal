(H, W, K) = list(map(int, input().split()))
table = [input() for _ in range(H)]
ans = 0
for mask_h in range(2 ** H):
    for mask_w in range(2 ** W):
        black = 0
        for i in range(H):
            for j in range(W):
                if mask_h >> i & 1 == 0 and mask_w >> j & 1 == 0 and (table[i][j] == '#'):
                    black += 1
        if black == K:
            ans += 1
print(str(ans))

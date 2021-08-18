H, W, K = map(int, input().split())
C = [list(input()) for _ in range(H)]

ans = 0
for row in range(2 ** H - 1):
    for col in range(2 ** W - 1):
        count = 0
        for i in range(H):
            for j in range(W):
                if not ((row >> i) & 1) and not ((col >> j) & 1) and C[i][j] == '
                count += 1
        if count == K:
            ans += 1

print(ans)

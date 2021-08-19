from sys import stdin
(H, W, K) = [int(_) for _ in stdin.readline().rstrip().split()]
C = [list(stdin.readline().rstrip()) for _ in range(H)]
ans = 0
for h in range(1 << H):
    for w in range(1 << W):
        black = 0
        for i in range(H):
            for j in range(W):
                if h >> i & 1 == 0 and w >> j & 1 == 0 and (C[i][j] == '#'):
                    black += 1
        if black == K:
            ans += 1
print(ans)

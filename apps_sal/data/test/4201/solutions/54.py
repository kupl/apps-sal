import sys

H, W, K = list(map(int, input().split()))

c = []
for i in range(H):
    c.append(list(input()))

ans = 0
for i in range(2**H):
    for j in range(2**W):
        count = 0
        for h in range(H):
            for w in range(W):
                if (i >> h) & 1 & (j >> w) & 1:
                    if c[h][w] == '
                    count += 1
        if count == K:
            ans += 1
print(ans)

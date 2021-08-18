H, W, K = list(map(int, input().split()))
c = [input() for _ in range(H)]

ans = 0
for R in range(2**H):
    for C in range(2**W):
        n = 0
        for y in range(H):
            if R >> y & 1:
                for x in range(W):
                    if C >> x & 1:
                        if c[y][x] == "
                        n += 1
        if n == K:
            ans += 1
print(ans)

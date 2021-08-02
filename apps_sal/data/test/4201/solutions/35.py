H, W, K = map(int, input().split())
c = [input() for _ in range(H)]
r = [[0] * W for _ in range(H)]
S = 0
for i in range(2**H):
    for j in range(2**W):
        cnt = 0
        for k in range(H):
            for l in range(W):
                if (i >> k) & 1:
                    if (j >> l) & 1:
                        if c[k][l] == "#":
                            cnt += 1
        if cnt == K:
            S += 1
print(S)

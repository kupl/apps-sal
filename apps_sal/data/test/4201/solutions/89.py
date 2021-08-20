(H, W, K) = map(int, input().split())
c = []
for i in range(H):
    c.append(list(input()))
ans = 0
for i in range(1 << H):
    for j in range(1 << W):
        v = 0
        for k in range(H):
            for l in range(W):
                if c[k][l] == '#' and i >> k & 1 == 0 and (j >> l & 1 == 0):
                    v += 1
        if v == K:
            ans += 1
print(ans)

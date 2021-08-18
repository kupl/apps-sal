H, W, K = map(int, input().split())
lis = []
ans = 0
for i in range(H):
    lis.append(list(input()))
for i in range(1 << H):
    for j in range(1 << W):
        cnt = 0
        for p in range(H):
            for q in range(W):
                if (i >> p) & 1:
                    continue
                if (j >> q) & 1:
                    continue
                if lis[p][q] == "
                cnt += 1
        if cnt == K:
            ans += 1
print(ans)

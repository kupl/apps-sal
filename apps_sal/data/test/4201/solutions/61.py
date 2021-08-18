h, w, K = map(int, input().split())
masu = [input() for _ in range(h)]
ans = 0
for i in range(2**h):
    for j in range(2**w):
        cnt = 0
        for k in range(h):
            for l in range(w):
                if ((i >> k) & 1) and ((j >> l) & 1) and masu[k][l] == "
                cnt += 1
        if cnt == K:
            ans += 1

print(ans)

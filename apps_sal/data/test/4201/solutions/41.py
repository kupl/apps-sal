H, W, K = map(int, input().split())
S = [input() for _ in range(H)]
ans = 0
for h in range(2**H):
    h = bin(h)[2:].zfill(H)
    for w in range(2**W):
        w = bin(w)[2:].zfill(W)
        cnt = 0
        for i in range(H):
            if h[i] == '1': continue
            for j in range(W):
                if w[j] == '1': continue
                if S[i][j] == '#':
                    cnt += 1

        if cnt == K:
            ans += 1

print(ans)

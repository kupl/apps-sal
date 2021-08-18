H, W, K = list(map(int, input().split()))
S = [list(input()) for _ in range(H)]
ans = 0

for H_mask in range(2**H):
    for W_mask in range(2**W):
        cnt = 0
        for i in range(H):
            for j in range(W):
                if (H_mask >> i) & 1 == 0 and (W_mask >> j) & 1 == 0\
                    and S[i][j] == '
                cnt += 1
        if cnt == K:
            ans += 1

print(ans)

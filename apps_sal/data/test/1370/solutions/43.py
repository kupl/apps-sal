import itertools

# input
H, W, K = list(map(int, input().split()))
S = [list(map(int, input())) for _ in range(H)]

# process
ans = H*W

for divr in range(1<<(H-1)):    # 横方向の分割を総当たり
    row = 0
    Sr = [[S[0][i] for i in range(W)]]
    for i in range(1, H):
        if 1&(divr>>i-1):
            row += 1
            Sr.append([S[i][j] for j in range(W)])
        else:
            Sr[row] = [Sr[row][j]+S[i][j] for j in range(W)]

    # 縦方向の分割を加算
    cnt = [0]*(row+1)
    ans_ = row
    flg = True
    for i in range(W):
        for j in range(row+1):
            if Sr[j][i] > K:
                flg = False
                break
            cnt[j] += Sr[j][i]
            if cnt[j] > K:
                ans_ += 1
                cnt = [0]*(row+1)
                for l in range(row+1):
                    cnt[l] += Sr[l][i]
                break

        if ans_ >= ans or not flg:
            break

    if flg:
        ans = min(ans, ans_)

# output
print(ans)


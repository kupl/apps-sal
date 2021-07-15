H, W = map(int,input().split())
S = []
for _ in range(H):
    S.append(list(input()))
for i in range(H):
    for j in range(W):
        if S[i][j] == '.':
            cnt = 0
            for k in range(-1, 2):
                for l in range(-1, 2):
                    if 0 <= i + k < H and 0 <= j + l < W and S[i+k][j+l] == '#':
                        cnt += 1
            S[i][j] = str(cnt)
for i in range(H):
    print(''.join(S[i]))

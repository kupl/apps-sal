l = [int(c) for c in input().split()]
H = l[0]
W = l[1]
S = [input() for c in range(H)]

for i in range(H):
    for j in range(W):
        if S[i][j] == ".":
            cnt = 0
            for k in range(3):
                for m in range(3):
                    if 0 <= i - 1 + k and i - 1 + k <= H - 1 and 0 <= j - 1 + m and j - 1 + m <= W - 1:
                        if S[i - 1 + k][j - 1 + m] == "
                        cnt += 1
            S[i] = S[i][:j] + str(cnt) + S[i][j + 1:]
    print(S[i])

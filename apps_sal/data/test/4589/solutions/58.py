(H, W) = map(int, input().split())
S = [list(input()) for i in range(H)]
dh = [0, 1, -1, 0, 1, -1, -1, 1]
dw = [1, 0, 0, -1, 1, 1, -1, -1]
for h in range(H):
    for w in range(W):
        if S[h][w] == '#':
            continue
        else:
            cnt = 0
            for k in range(8):
                next_h = h + dh[k]
                next_w = w + dw[k]
                if not 0 <= next_h <= H - 1 or not 0 <= next_w <= W - 1:
                    continue
                elif S[next_h][next_w] == '#':
                    cnt += 1
        S[h][w] = str(cnt)
for s in S:
    print(''.join(s))

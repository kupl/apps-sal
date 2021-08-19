(H, W) = map(int, input().split())
S = []
for _ in range(H):
    s = list(input())
    S.append(s)
cnt = [[0] * W for _ in range(H)]
for h in range(H):
    c = 0
    for w in range(W):
        if S[h][w] == '#':
            c += 1
        else:
            if c == 1:
                cnt[h][w - 1] = 1
            c = 0
    if c == 1:
        cnt[h][w] = 1
ans = 'Yes'
for w in range(W):
    c = 0
    for h in range(H):
        if S[h][w] == '#':
            c += 1
        else:
            if c == 1:
                if cnt[h - 1][w] == 1:
                    ans = 'No'
                    break
            c = 0
    if c == 1:
        if cnt[h][w] == 1:
            ans = 'No'
            break
print(ans)

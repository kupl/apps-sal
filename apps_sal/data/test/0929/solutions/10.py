(H, W) = list(map(int, input().split()))
a = [0] * H
for i in range(H):
    if i % 2 == 0:
        a[i] = list(map(int, input().split()))
    else:
        a[i] = list(map(int, input().split()))[::-1]
s = [[0] * W for i in range(H)]
s[0][0] = a[0][0] % 2
for i in range(1, W):
    s[0][i] = (s[0][i - 1] + a[0][i]) % 2
for i in range(1, H):
    for j in range(W):
        if j == 0:
            s[i][j] = (s[i - 1][-1] + a[i][j]) % 2
        else:
            s[i][j] = (s[i][j - 1] + a[i][j]) % 2
s[H - 1][W - 1] = 0
ans = []
for i in range(H):
    for j in range(W):
        if s[i][j]:
            if i % 2 == 0:
                if j != W - 1:
                    ans.append([i + 1, j + 1, i + 1, j + 2])
                else:
                    ans.append([i + 1, j + 1, i + 2, j + 1])
            elif j != W - 1:
                ans.append([i + 1, W - j, i + 1, W - j - 1])
            else:
                ans.append([i + 1, W - j, i + 2, W - j])
print(len(ans))
for i in range(len(ans)):
    print('{} {} {} {}'.format(ans[i][0], ans[i][1], ans[i][2], ans[i][3]))

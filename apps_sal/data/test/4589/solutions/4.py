h, w = list(map(int, input().split()))
s = [list(map(str, input())) for i in range(h)]
ans = s

di = [1, 0, -1, 0, 1, -1, -1, 1]
dj = [0, 1, 0, -1, 1, 1, -1, -1]

for i in range(h):
    for j in range(w):
        if s[i][j] == '
        continue
        cnt = 0
        for d in range(8):
            if i + di[d] < 0 or i + di[d] > h - 1 or j + dj[d] < 0 or j + dj[d] > w - 1:
                continue
            if s[i + di[d]][j + dj[d]] == '
            cnt += 1
        ans[i][j] = cnt

for i in range(h):
    print((''.join(map(str, ans[i]))))

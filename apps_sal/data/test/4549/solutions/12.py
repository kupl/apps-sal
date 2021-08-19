h, w = list(map(int, input().split()))
s = [input() for _ in range(h)]

dh = [0, 1, 0, -1]
dw = [1, 0, -1, 0]
flag = 0

for i in range(h):
    for j in range(w):
        if s[i][j] == '#':
            cnt = 0
            for p in range(4):
                if i + dh[p] < 0 or i + dh[p] >= h or j + dw[p] < 0 or j + dw[p] >= w:
                    continue
                else:
                    if s[i + dh[p]][j + dw[p]] == '#':
                        cnt += 1
            if cnt == 0:
                flag = 1
                break
        if flag == 1:
            break
    if flag == 1:
        print('No')
        break
else:
    print('Yes')

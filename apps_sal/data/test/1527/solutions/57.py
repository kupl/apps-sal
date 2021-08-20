import math
import sys
sys.setrecursionlimit(10000)
(H, W) = map(int, input().split())
S = []
for i in range(H):
    S.append(str(input()))


def main(l, d, cnt):
    tmp = []
    for n in l:
        (i, j) = (n[0], n[1])
        if 0 < i and S[i - 1][j] == '.':
            if d[i - 1][j] > d[i][j] + 1:
                d[i - 1][j] = d[i][j] + 1
                tmp.append([i - 1, j])
        if i < H - 1 and S[i + 1][j] == '.':
            if d[i + 1][j] > d[i][j] + 1:
                d[i + 1][j] = d[i][j] + 1
                tmp.append([i + 1, j])
        if 0 < j and S[i][j - 1] == '.':
            if d[i][j - 1] > d[i][j] + 1:
                d[i][j - 1] = d[i][j] + 1
                tmp.append([i, j - 1])
        if j < W - 1 and S[i][j + 1] == '.':
            if d[i][j + 1] > d[i][j] + 1:
                d[i][j + 1] = d[i][j] + 1
                tmp.append([i, j + 1])
    if tmp == []:
        return cnt
    else:
        cnt += 1
        return main(tmp, d, cnt)


ans = 0
for i in range(H):
    for j in range(W):
        if S[i][j] == '.':
            d = [[float('inf') for i in range(W)] for j in range(H)]
            d[i][j] = 0
            cnt = main([[i, j]], d, 0)
            ans = max(ans, cnt)
print(ans)

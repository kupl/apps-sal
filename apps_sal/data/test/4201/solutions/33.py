import copy
(H, W, K) = list(map(int, input().split()))
d = {}
ans = 0
for i in range(H):
    d['c' + str(i)] = list(input())


def changeRow(d, num, W):
    d['c' + str(num)] = ['.'] * W


def changeColum(d, num, H):
    for i in range(H):
        d['c' + str(i)][num] = '.'


def checkSharp(d, H):
    cnt = 0
    for i in range(H):
        cnt += d['c' + str(i)].count('#')
    return cnt


for i in range(2 ** W):
    for j in range(2 ** H):
        dCopy = copy.deepcopy(d)
        for k in range(W):
            if i >> k & 1:
                changeColum(dCopy, k, H)
        for k in range(H):
            if j >> k & 1:
                changeRow(dCopy, k, W)
        if K == checkSharp(dCopy, H):
            ans += 1
print(ans)

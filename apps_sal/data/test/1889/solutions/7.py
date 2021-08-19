import time


def res(row):
    ans = 0
    buf = 0
    for i in row:
        if i == 1:
            buf += 1
        elif buf != 0:
            ans = max(ans, buf)
            buf = 0
    ans = max(ans, buf)
    return ans


(n, m, q) = (int(i) for i in input().split())
desk = []
score = []
start = time.time()
for j in range(n):
    row = [int(i) for i in input().split()]
    desk.append(row)
    score.append(res(row))
ans = []
for k in range(q):
    (i, j) = (int(l) for l in input().split())
    i -= 1
    j -= 1
    desk[i][j] = 1 if desk[i][j] == 0 else 0
    score[i] = res(desk[i])
    ans.append(max(score))
for i in ans:
    print(i)
finish = time.time()

n = int(input())
X = [[0] * 7 for _ in range(n)]
for i in range(n):
    (x, y) = map(int, input().split())
    X[i][0] = i + 1
    X[i][1] = x
    X[i][2] = y
C = [int(i) for i in input().split()]
K = [int(i) for i in input().split()]
for i in range(n):
    X[i][3] = C[i]
    X[i][4] = K[i]
ans_am = 0
ans_ps = 0
Ans = []
ans_con = 0
Con = []


def m(X):
    ret = 0
    cur = X[0][3]
    for i in range(1, len(X)):
        if X[i][3] < cur:
            ret = i
            cur = X[i][3]
    return ret


while X:
    r = m(X)
    (ind, x, y, c, k, flag, source) = X.pop(r)
    ans_am += c
    if flag == 0:
        ans_ps += 1
        Ans.append(ind)
    else:
        ans_con += 1
        Con.append([ind, source])
    for i in range(len(X)):
        (indi, xi, yi, ci, ki, flagi, sourcei) = X[i]
        if (k + ki) * (abs(x - xi) + abs(y - yi)) < ci:
            X[i][3] = (k + ki) * (abs(x - xi) + abs(y - yi))
            X[i][5] = 1
            X[i][6] = ind
print(ans_am)
print(ans_ps)
print(*Ans)
print(ans_con)
for (i, j) in Con:
    print(i, j)

x1, y1 = list(map(int, input().split()))
x2, y2 = list(map(int, input().split()))
n = int(input())
s = input()

x, y = x2 - x1, y2 - y1
X = [[0, 0] for i in range(n + 1)]
for i in range(n):
    if s[i] == "U":
        X[i + 1] = [X[i][0], X[i][1] + 1]
    elif s[i] == "D":
        X[i + 1] = [X[i][0], X[i][1] - 1]
    elif s[i] == "L":
        X[i + 1] = [X[i][0] - 1, X[i][1]]
    elif s[i] == "R":
        X[i + 1] = [X[i][0] + 1, X[i][1]]


def chk(k):
    nonlocal x, y
    # print("chk", k)
    for i in range(n):
        xt = X[i][0]
        yt = X[i][1]
        if abs(xt + X[n][0] * k - x) + abs(yt + X[n][1] * k - y) <= k * n + i:
            # print(k, n, i, k*n+i)
            return k * n + i

    return -1


def chklr(l, r, ma):
    if l + 1 == r:
        return ma
    m = (l + r) // 2
    tmp = chk(m)
    if tmp < 0:
        return chklr(m, r, ma)
    else:
        return chklr(l, m, tmp)

# print(X)


if chk(10**15) < 0:
    print(-1)
else:
    print(chklr(-1, 10**15, chk(10**15)))

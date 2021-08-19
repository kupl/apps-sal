(w, h, n) = map(int, input().split())
(x, y, a) = ([], [], [])
for i in range(n):
    (X, Y, A) = map(int, input().split())
    x.append(X)
    y.append(Y)
    a.append(A)
zahyou = [[1 for _ in range(h)] for __ in range(w)]


def m1(d):
    for i in range(d):
        for j in range(h):
            zahyou[i][j] = 0


def m2(d):
    for i in range(w - d):
        for j in range(h):
            zahyou[i + d][j] = 0


def m3(d):
    for i in range(w):
        for j in range(d):
            zahyou[i][j] = 0


def m4(d):
    for i in range(w):
        for j in range(h - d):
            zahyou[i][j + d] = 0


for i in range(n):
    if a[i] == 1:
        m1(x[i])
    elif a[i] == 2:
        m2(x[i])
    elif a[i] == 3:
        m3(y[i])
    else:
        m4(y[i])
print(sum(map(sum, zahyou)))

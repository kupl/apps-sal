N = int(input())
xyd = [list(input().split()) for _ in range(N)]


def nasu(s, e, f, n, inf):
    L = [0] * 3
    a, b, c = inf, inf, inf
    for i in range(N):
        t = int(xyd[i][n])
        if xyd[i][2] == s:
            a = f(a, t)
        elif xyd[i][2] == e:
            b = f(b, t)
        else:
            c = f(c, t)
    L[0] = a
    if f(a, c) == a:
        L[1] = abs(a - c)
    else:
        L[0], L[1] = c, 0
    if f(L[0], b) != b:
        if f(c, b) == c:
            L[2] = abs(b - c)
            if L[1] > L[2]:
                L[2] = abs(a - b) / 2
                L[1] = L[2]
        else:
            L[2] = abs(a - b) / 2
            L[1] = L[2]
    else:
        L = [b, 0, 0]
    for i in range(3):
        if abs(L[i]) > abs(inf) / 2:
            L[i] = abs(inf)
    return L


inf = 10 ** 10
R = nasu("L", "R", max, 0, -inf)
L = nasu("R", "L", min, 0, inf)
U = nasu("D", "U", max, 1, -inf)
D = nasu("U", "D", min, 1, inf)


def honya(x):
    r = honyaraka(R, x, 1)
    l = honyaraka(L, x, -1)
    u = honyaraka(U, x, 1)
    d = honyaraka(D, x, -1)
    return abs(r - l) * abs(u - d)


def honyaraka(X, x, f):
    a, b, c = X
    if x <= b:
        return a + x * f * -1
    if x < c:
        return a + b * f * -1
    return a + b * f * -1 + (x - c) * f


ans = honya(0)
T = [R, L, U, D]
for i in range(4):
    for j in range(1, 3):
        x = T[i][j]
        if x != inf:
            ans = min(ans, honya(x))

print(ans)

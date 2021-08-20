(n, bx) = list(map(int, input().split()))
X = list(map(int, input().split()))
(m, by) = list(map(int, input().split()))
Y = list(map(int, input().split()))


def calcul(n, bx, X):
    r = X[n - 1]
    c = 1
    for k in range(2, n + 1):
        c *= bx
        r += X[n - k] * c
    return r


x = calcul(n, bx, X)
y = calcul(m, by, Y)
if x == y:
    print('=')
elif x > y:
    print('>')
else:
    print('<')

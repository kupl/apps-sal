def read():
    return list(map(int, input().split()))


def f(a, x, y):
    return (a * x + x + y - 1) // (x + y)


(n, x, y) = read()
for i in range(n):
    a = int(input())
    d = f(a, x, y) * y - f(a, y, x) * x
    if d < 0:
        res = 'Vanya'
    elif d > 0:
        res = 'Vova'
    elif d == 0:
        res = 'Both'
    print(res)

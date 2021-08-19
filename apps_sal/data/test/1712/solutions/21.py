(n, x, y) = list(map(int, input().split()))


def fun(a1, x1, y1):
    return (a1 * x1 + x1 + y1 - 1) // (x + y)


for _ in range(n):
    a = int(input())
    op1 = fun(a, x, y) * y
    op2 = fun(a, y, x) * x
    if op1 == op2:
        print('Both')
    elif op1 < op2:
        print('Vanya')
    elif op1 > op2:
        print('Vova')

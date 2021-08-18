n, a = list(map(int, input().split()))
x = list(map(int, input().split()))


def visit(a, b, c):
    if a <= b:
        return c - a
    if a >= c:
        return a - b
    return c - b + min(c - a, a - b)


x.sort()
if n <= 1:
    print(0)
elif a <= x[0]:
    print(x[-2] - a)
elif a >= x[-1]:
    print(a - x[1])
else:
    print(min(visit(a, x[0], x[-2]), visit(a, x[1], x[-1])))

from math import sqrt
a, b, c = list(map(float, input().split()))
x1, y1, x2, y2 = list(map(float, input().split()))


def main():
    nonlocal a, b, c, x1, y1, x2, y2
    if (b == 0 or a == 0):
        return (abs(x1 - x2) + abs(y1 - y2))

    AD, AC, DB, CB = False, False, False, False
    def y(x0): return -c / b - a / b * x0
    def x(y0): return -c / a - b / a * y0
    def r(x1, y1, x2, y2): return sqrt((x1 - x2)**2 + (y1 - y2)**2)
    def yes(x1, x, x2): return (min(x1, x2) <= x and x <= max(x1, x2))
    '''print(x(y1), x(y2), y(x1), y(x2))'''
    if (yes(y1, y(x1), y2) and yes(y1, y(x2), y2)):
        '''print(1)'''
        e = abs(y(x1) - y1)
        f = abs(y(x2) - y2)
        g = r(x1, y(x1), x2, y(x2))
        '''print(e, f, g)'''
        return (e + f + g)

    if (yes(y1, y(x1), y2) and yes(x1, x(y2), x2)):
        '''print(2)'''
        e = abs(y(x1) - y1)
        f = abs(x(y2) - x2)
        g = r(x1, y(x1), x(y2), y2)
        '''print(e, f, g)'''
        return (e + f + g)

    if (yes(x1, x(y1), x2) and yes(x1, x(y2), x2)):
        '''print(3)'''
        e = abs(x(y1) - x1)
        f = abs(x(y2) - x2)
        g = r(x(y1), y1, x(y2), y2)
        '''print(e, f, g)'''
        return (e + f + g)

    if (yes(x1, x(y1), x2) and yes(y1, y(x2), y2)):
        '''print(4)'''
        e = abs(x(y1) - x1)
        f = abs(y(x2) - y2)
        g = r(x(y1), y1, x2, y(x2))
        '''print(e, f, g)'''
        return (e + f + g)

    '''print("none returned!")'''
    return (abs(x1 - x2) + abs(y1 - y2))


ans = main()
straight = abs(x1 - x2) + abs(y1 - y2)
print(min(ans, straight))

import numpy
a = list(input())
b = list(input())
c = list(input())


def check(x='a'):
    try:
        if x == 'a':
            x = a.pop(0)
            check(x)
        elif x == 'b':
            x = b.pop(0)
            check(x)
        elif x == 'c':
            x = c.pop(0)
            check(x)
    except IndexError:
        print(x.upper())


check()

from fractions import gcd

def lcd(a, b):
    g = gcd(a, b)
    return a*b//g

def __starting_point():
    x, y, a, b = [int(x) for x in input().split()]
    l = lcd(x, y)
    r = a%l
    if r == 0:
        print((b-a)//l+1)
    else:
        print((b-(a+(l-r)))//l+1)

__starting_point()

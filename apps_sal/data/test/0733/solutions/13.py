from fractions import gcd

def lcd(a, b):
    g = gcd(a, b)
    return a*b//g

def __starting_point():
    x, y, a, b = [int(x) for x in input().split()]
    l = lcd(x, y)
    print(b//l-(a-1)//l)

__starting_point()

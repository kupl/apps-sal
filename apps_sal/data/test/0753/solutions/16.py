from fractions import Fraction
while(1):
    try:
        a, b, c, d = list(map(int, input().split()))
        if a / b < c / d:
            ratio = 0
        elif a / b == c / d:
            ratio = -1
        else:
            ratio = 1
        if ratio == 0:
            f = Fraction(b * c - a * d, b * c)
            print("%s" % (f))
        elif ratio == 1:
            f = Fraction(a * d - b * c, a * d)
            print("%s" % (f))
        else:
            print("0/1")
    except EOFError:
        break

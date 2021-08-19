from fractions import Fraction


def __starting_point():
    inp = input()
    arr = inp.split(' ')
    a = Fraction(int(arr[0]), 1)
    b = Fraction(int(arr[1]), 1)
    c = Fraction(int(arr[2]), 1)
    d = Fraction(int(arr[3]), 1)
    if d * a == c * b:
        ans = Fraction(0, 1)
    elif d * a < c * b:
        ans = (b - d * (a / c)) / b
    else:
        ans = (a - c * (b / d)) / a
    print(ans.numerator, end='')
    print('/', end='')
    print(ans.denominator)


__starting_point()

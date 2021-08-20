def isValid(x):
    if x >= 0 and x.is_integer():
        return True


def main():
    (n1, n2, n3) = [int(x) for x in input().split()]
    a = 0.5 * (n3 - n2 + n1)
    b = n3 - a
    c = n1 - a
    if isValid(a) and isValid(b) and isValid(c):
        print(' '.join((str(int(x)) for x in [c, b, a])))
    else:
        print('Impossible')


main()

def is_YY(S):
    N = int(S)
    if 00 <= N <= 99:
        return True
    else:
        return False


def is_MM(S):
    N = int(S)
    if 1 <= N <= 12:
        return True
    else:
        return False


def __starting_point():
    S = input()
    top = S[:2]
    bottom = S[2:]
    if is_YY(top) and is_MM(top) and is_YY(bottom) and is_MM(bottom):
        print('AMBIGUOUS')
    elif is_YY(top) and is_MM(bottom):
        print('YYMM')
    elif is_MM(top) and is_YY(bottom):
        print('MMYY')
    else:
        print('NA')


__starting_point()

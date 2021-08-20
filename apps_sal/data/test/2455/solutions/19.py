def test_col(s, a, b, col):
    res = True
    for i in range(0, a):
        if s[i * b + col] != 'X':
            res = False
    return res


def test_all_cols(s, a):
    b = len(s) // a
    if a * b != len(s):
        return False
    else:
        res = False
        for i in range(0, b):
            res = res or test_col(s, a, b, i)
        return res


n = int(input())
for i in range(0, n):
    s = input()
    slen = len(s)
    cvariants = 0
    variants = ''
    for a in range(1, slen + 1):
        if test_all_cols(s, a):
            cvariants += 1
            variants += str(a) + 'x' + str(slen // a) + ' '
    print(str(cvariants), variants)

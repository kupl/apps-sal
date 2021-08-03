def clz(s):
    n = 0
    for i in range(len(s)):
        if s[i] == '0':
            n += 1
        else:
            break
    return n


def solve():
    A = input()
    B = input()

    lza = clz(A)
    lzb = clz(B)

    la = len(A) - lza
    lb = len(B) - lzb

    if la > lb:
        print('>')
    elif la < lb:
        print('<')
    else:
        for i in range(la):
            if A[lza + i] > B[lzb + i]:
                print('>')
                break
            elif A[lza + i] < B[lzb + i]:
                print('<')
                break
        else:
            print('=')


def __starting_point():
    solve()


__starting_point()

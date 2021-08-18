
def tk(s):
    s1 = s[0:len(s) // 2 + 1]
    s2 = s[len(s) // 2:len(s)]

    if s1 == s2[::-1]:
        return True
    else:
        return False


def Kaibun(s):
    if s == s[::-1]:
        return True
    else:
        return False


def __starting_point():
    S = input()

    if tk(S) and Kaibun(S[0:len(S) // 2]) and Kaibun(S[len(S) // 2 + 1:len(S)]):
        print('Yes')

    else:
        print('No')


__starting_point()

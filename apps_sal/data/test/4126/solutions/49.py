def readinput():
    s = input()
    return s


def isKaibun(s):
    i = 0
    j = len(s) - 1
    while i <= j:
        if s[i] != s[j]:
            return False
        else:
            i += 1
            j -= 1
    return True


def main(s):
    if not isKaibun(s):
        return 'No'
    n = len(s)
    m = (n - 1) // 2
    l = (n + 3) // 2
    if not isKaibun(s[:m]):
        return 'No'
    if not isKaibun(s[l - 1:]):
        return 'No'
    return 'Yes'


def __starting_point():
    s = readinput()
    ans = main(s)
    print(ans)


__starting_point()

def readinput():
    s = input()
    return s


def main(s):
    if s[0] != 'A':
        return 'WA'
    if s[2:-1].count('C') != 1:
        return 'WA'
    ls = s.lower()
    count = 0
    for i, c in enumerate(s):
        if c != ls[i]:
            count += 1
    if count != 2:
        return 'WA'
    else:
        return 'AC'


def __starting_point():
    s = readinput()
    ans = main(s)
    print(ans)


__starting_point()

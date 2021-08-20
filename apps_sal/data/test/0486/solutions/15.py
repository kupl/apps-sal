s = input()


def chuj(st, le):
    if le == 1:
        return int(st)
    return max(max(int(st[0]) - 1, 1) * 9 ** (le - 1), int(st[0]) * chuj(st[1:], le - 1))


print(chuj(s, len(s)))

s1 = input()
s2 = input()


def Sort(string):
    l = len(string)
    if l % 2 == 1:
        return string
    s1 = Sort(string[:l // 2])
    s2 = Sort(string[l // 2:])
    if s1 < s2:
        return s1 + s2
    else:
        return s2 + s1


if Sort(s1) == Sort(s2):
    print('YES')
else:
    print('NO')

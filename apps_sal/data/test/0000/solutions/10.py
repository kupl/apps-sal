s = input()


def sovle(s):
    i1 = s.find('[')
    if i1 == -1:
        return -1
    s = s[i1 + 1:]
    i2 = s.find(':')
    if i2 == -1:
        return -1
    s = s[i2 + 1:]
    i1 = s.rfind(']')
    if i1 == -1:
        return -1
    s = s[:i1]
    i2 = s.rfind(':')
    if i2 == -1:
        return -1
    s = s[:i2]
    x = s.count('|')
    return x + 4


print(sovle(s))

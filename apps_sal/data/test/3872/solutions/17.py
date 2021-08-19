def getmin(s):
    ls = len(s)
    if ls % 2 == 1:
        return s
    s1 = getmin(s[:ls // 2])
    s2 = getmin(s[ls // 2:])
    return s1 + s2 if s1 < s2 else s2 + s1


s1 = input()
s2 = input()
print('YES') if getmin(s1) == getmin(s2) else print('NO')

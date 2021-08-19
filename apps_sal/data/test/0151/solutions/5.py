def findO(s):
    glas = {'a', 'e', 'i', 'o', 'u'}
    i = 0
    while i < len(s) - 2:
        newSet = {s[i], s[i + 1], s[i + 2]}
        if len(newSet & glas) == 0 and (not s[i] == s[i + 1] == s[i + 2]):
            s1 = s[:i + 2]
            s2 = s[i + 2:]
            s = s1 + ' ' + s2
            i += 3
        else:
            i += 1
    return s


s = input()
s = findO(s)
print(s)

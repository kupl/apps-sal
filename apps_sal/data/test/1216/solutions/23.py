n = input()
s = input()
x = ""
x += s[0]
for i in range(1, len(s)):
    if s[i] != s[i - 1]:
        x += ' '
        x += s[i]
    else:
        x += s[i]
x = x.split()
res = ""
for i in x:
    if (i[0] == 'a'):
        res += 'a'
        continue
    if (i[0] == 'y'):
        res += 'y'
        continue
    if (i[0] == 'i'):
        res += 'i'
        continue
    if (i[0] == 'u'):
        res += 'u'
        continue
    if (i[0] == 'e'):
        if (len(i) != 2):
            res += 'e'
        else:
            res += 'ee'
        continue
    if (i[0] == 'o'):
        if (len(i) != 2):
            res += 'o'
        else:
            res += 'oo'
        continue
    res += i
print(res)

s = input()
a = ''
l = len(s)
for i in range(len(s)):
    if (i % 2 == 0):
        if (l % 2 == 0):
            a = s[-1] + a
            s = s[:-1]
        else:
            a = s[0] + a
            s = s[1:]
    else:
        if (l % 2 == 0):
            a = s[0] + a
            s = s[1:]
        else:
            a = s[-1] + a
            s = s[:-1]
print(a)

s = input()
m = ord(s[0])
for i in range(0, len(s)):
    a = ord(s[i])
    f = False
    if a > m:
        f = True
    else:
        m = a
    print('Mike' if not f else 'Ann')

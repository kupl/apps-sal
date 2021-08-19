t = int(input())
for i in range(t):
    re = []
    s = str(input())
    l = len(s)
    for j in range(l - 4):
        if s[j:j + 5] == 'twone':
            re.append(j + 2)
        elif s[j:j + 3] == 'two':
            re.append(j + 1)
        elif s[j:j + 3] == 'one':
            if j >= 2:
                if s[j - 2:j + 3] != 'twone':
                    re.append(j + 1)
            else:
                re.append(j + 1)
    if (s[l - 4:l - 1] == 'one' or s[l - 4:l - 1] == 'two') and s[l - 6:-1] != 'twone':
        re.append(l - 3)
    if (s[l - 3:] == 'one' or s[l - 3:] == 'two') and s[l - 5:] != 'twone':
        re.append(l - 2)
    le = len(re)
    print(le)
    for d in range(le):
        print(re[d] + 1, end=' ')
    print()

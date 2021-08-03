s = input()
l = list(set(s))
ans = 1
if (len(l) > 4) or (len(l) <= 1):
    ans = 0
else:
    if len(l) == 2:
        c1 = 0
        c0 = 0
        for i in range(len(s)):
            if s[i] == l[0]:
                c0 += 1
            else:
                c1 += 1
        if (c1 < 2) or (c0 < 2):
            ans = 0
    if (len(l) == 3):
        c1 = 0
        c2 = 0
        c0 = 0
        for i in range(len(s)):
            if s[i] == l[0]:
                c0 += 1
            if s[i] == l[1]:
                c1 += 1
            if s[i] == l[2]:
                c2 += 1
        if (c1 + c2 + c0) < 4:
            ans = 0
if (ans == 0):
    print('No')
else:
    print('Yes')

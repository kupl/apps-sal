for i in range(int(input())):
    s = input()
    t = input()
    j = 0
    i = 0
    if len(t) < len(s):
        print('NO')
        continue
    while i < len(s):
        f = True
        cu = s[i]
        cou = 1
        i += 1
        while i < len(s) and s[i] == cu:
            cou += 1
            i += 1
        while cou > 0:
            if j >= len(t) or t[j] != cu:
                f = False
                break
            else:
                cou -= 1
                j += 1
        if not f:
            break
        while j < len(t) and t[j] == cu:
            j += 1
    if f and j == len(t):
        print('YES')
    else:
        print('NO')

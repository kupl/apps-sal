n = int(input())
s = input()
if len(s) == 1:
    print(s)
else:
    co = 0
    ce = 0
    ca = 0
    cy = 0
    cu = 0
    ci = 0
    r = ''
    s += '0'

    for i in range(0, len(s) - 1):
        p = True
        p1 = False

        if s[i] == 'o':
            p = False
            co += 1
            p = co == 1 and s[i + 1] != 'o'
            if p == False:
                p = co > 2 and s[i + 1] != 'o'
            if p == False:
                p1 = co == 2 and s[i + 1] != 'o'
        else:
            co = 0

        if s[i] == 'e':
            p = False
            ce += 1
            p = ce == 1 and s[i + 1] != 'e'
            if p == False:
                p = ce > 2 and s[i + 1] != 'e'
            if p == False:
                p1 = ce == 2 and s[i + 1] != 'e'
        else:
            ce = 0

        if s[i] == 'a':
            ca += 1
            p = ca == 1
        else:
            ca = 0

        if s[i] == 'u':
            cu += 1
            p = cu == 1
        else:
            cu = 0

        if s[i] == 'i':
            ci += 1
            p = ci == 1
        else:
            ci = 0

        if s[i] == 'y':
            cy += 1
            p = cy == 1
        else:
            cy = 0

        if p1:
            r += s[i] + s[i]
        if p:
            r += s[i]
    print(r)

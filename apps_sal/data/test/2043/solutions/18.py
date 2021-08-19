def search_podstroki(t, s):
    c1 = 0
    for i in range(len(t)):
        if t[i] == s[0]:
            s = s[1:]
            if len(s) == 0:
                c1 = -1
                return i + 1
    if c1 == 0:
        return -1


s = input()
t = input()
e = 0
if len(t) <= len(s):
    print('0')
else:
    s1 = s
    h = search_podstroki(t, s1)
    s1 = s1[::-1]
    t = t[::-1]
    g = search_podstroki(t, s1)
    if g == -1 or h == -1:
        print('0')
    else:
        g = len(t) - g + 1
        if g < h:
            print('0')
        else:
            print(g - h)

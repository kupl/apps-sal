t = int(input())
for _ in range(t):
    s = input()
    l = len(s)
    r = set()
    for i in range(l - 2):
        if s[i] == 'o':
            if s[i + 1] == 'n':
                if s[i + 2] == 'e':
                    if i > 0:
                        if s[i - 1] != 'w':
                            r.add(i + 2)
                        else:
                            r.add(i + 1)
                    else:
                        r.add(i + 1)
        elif s[i] == 't':
            if s[i + 1] == 'w':
                if s[i + 2] == 'o':
                    if i + 3 < l:
                        if s[i + 3] != 'n':
                            r.add(i + 2)
                        else:
                            r.add(i + 3)
                    else:
                        r.add(i + 2)
    print(len(r))
    for el in r:
        print(el, end=' ')
    print()

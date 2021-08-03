a = int(input())
for i in range(a):
    g = input()
    p = 0
    one = str('one')
    two = str('two')
    ch = []
    for i in range(len(g) - 2):
        if g[i] == 'o':
            if g[i + 1] == 'n':
                if g[i + 2] == 'e':
                    if p == 0:
                        ch.append(i + 2)
                    else:
                        p = 0
        if g[i] == 't':
            if g[i + 1] == 'w':
                if g[i + 2] == 'o':
                    if len(g) - 1 >= i + 4:
                        if g[i + 3] == 'n' and g[i + 4] == 'e':
                            ch.append(i + 3)
                            p = 1
                        else:
                            ch.append(i + 2)
                    else:
                        ch.append(i + 2)
    print(len(ch))
    print(*ch)

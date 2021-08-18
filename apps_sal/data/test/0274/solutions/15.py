l = int(input())
n = input()


def offset(ml, x):
    return (ml - x) // 2


def getstate(g, line, ml):
    off = offset(ml, g[0])
    if line < off or line >= g[0] + off:
        return 0
    elif line == off or line == g[0] + off - 1:
        return 1
    else:
        return 2


ml = 1
cl = 1
for b in n:
    if b == '[':
        cl += 2
        if ml < cl:
            ml = cl
    else:
        cl -= 2
sc = []
for b in n:
    if b == '[':
        sc.append([ml, True])
        ml -= 2
    else:
        ml += 2
        sc.append([ml, False])
for i in range(ml):
    for j in range(l):
        g = sc[j]
        state = getstate(g, i, ml)
        if state == 1:
            if g[1]:
                print('+-', end='')
            else:
                print('-+', end='')
        elif state == 0:
            if sc[j - 1][0] - sc[j][0] != 2:
                print('  ', end='')
        else:
            print('|', end='')
        if sc[j][1] and not sc[j + 1][1]:
            if state == 2:
                print('   ', end='')
            else:
                print(' ', end='')

    print()

def actionA(i):
    return i // 2


def actionB(i):
    return (i - 1) // 10


def getAction(i):
    if not (i % 2):
        return actionA
    elif (i % 10) == 1:
        return actionB
    else:
        return None


def fail():
    print('NO')


def m():
    i, j = (int(a) for a in input().split(' '))
    l = [j]
    while True:
        act = getAction(j)
        if act is None:
            return fail()
        j = act(j)
        l.append(j)
        if j < i:
            return fail()
        if j == i:
            break
    l.reverse()
    print('YES', len(l), ' '.join(str(i) for i in l), sep='\n')  # success!


def __starting_point():
    m()


__starting_point()

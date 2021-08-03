
def f():
    N = int(input())
    UP = []
    DOWN = []

    for _ in range(N):
        S = input()
        c = 0
        minC = 0

        for s in S:
            if s == '(':
                c += 1
            else:
                c -= 1
                minC = min(minC, c)

        if c >= 0:
            UP.append((minC, c))
        else:
            DOWN.append((c - minC, c))

    c = 0
    for up in sorted(UP, reverse=True):
        if c + up[0] < 0:
            return False

        c += up[1]

    for down in sorted(DOWN, reverse=True):
        if c + down[1] - down[0] < 0:
            return False

        c += down[1]

    if c != 0:
        return False

    return True


if f():
    print('Yes')
else:
    print('No')

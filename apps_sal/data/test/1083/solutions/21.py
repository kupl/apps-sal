n = int(input())


def getg(n):
    if n % 4 == 0:
        return (0, list(range(n // 4 + 1, 3 * n // 4 + 1)))
    elif n % 4 == 1:
        return (1, [1] + [x + 1 for x in getg(n - 1)[1]])
    elif n % 4 == 2:
        return (1, getg(n - 2)[1] + [n - 1])
    elif n % 4 == 3:
        return (0, [1] + [x + 1 for x in getg(n - 1)[1]])


g = getg(n)
print(g[0])
print(str(len(g[1])) + ' ' + ' '.join(str(x) for x in g[1]))

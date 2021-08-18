from sys import maxsize as m


def __starting_point():
    n, p = list(map(int, input().split(' ')))

    c = m
    buyer = []
    cost = {}
    for i in range(n):
        buyer += [input()]
    a = 1
    for i in range(n - 2, -1, -1):
        if buyer[i] == 'half':
            a = 2 * a
        elif buyer[i] == 'halfplus':
            a = 2 * a + 1

    cost = 0
    for i in range(n):
        if a % 2 == 0:
            if buyer[i] == 'half':
                cost += p * (a / 2)
                a /= 2
            elif buyer[i] == 'halfplus':
                cost += p * (a / 2 - 1 / 2)
                a = int(a / 2 - 1 / 2)
        else:
            cost += p * (a / 2)
            a = int(a / 2 - 1 / 2)
    print(int(cost))


__starting_point()

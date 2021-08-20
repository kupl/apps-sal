from sys import stdin


def main():
    readline = stdin.readline
    n = int(readline())
    s = tuple((readline().strip() for _ in range(n)))
    (plus, minus) = ([], [])
    for c in s:
        if 2 * c.count('(') - len(c) > 0:
            plus.append(c)
        else:
            minus.append(c)
    plus.sort(key=lambda x: x.count(')'))
    minus.sort(key=lambda x: x.count('('), reverse=True)
    plus.extend(minus)
    sum = 0
    for v in plus:
        for vv in v:
            sum = sum + (1 if vv == '(' else -1)
            if sum < 0:
                return print('No')
    if sum != 0:
        return print('No')
    return print('Yes')


def __starting_point():
    main()


__starting_point()

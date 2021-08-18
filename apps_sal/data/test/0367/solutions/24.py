from bisect import insort


def main():
    wd = input()
    chars = dict()
    for c in wd:
        if c not in chars:
            chars[c] = 0
        chars[c] += 1
    odds = list()
    evens = list()

    for k, v in list(chars.items()):
        if v % 2:
            odds.append((k, v))
        else:
            evens.append((k, v))

    odds.sort()
    while len(odds) > 1:
        odds[0] = (odds[0][0], odds[0][1] + 1)
        odds[-1] = (odds[-1][0], odds[-1][1] - 1)
        if odds[-1][1] < 1:
            del odds[-1]
        elif odds[-1][1] % 2 == 0:
            evens.append(odds.pop())
        if odds[0][1] % 2 == 0:
            evens.append(odds[0])
            del odds[0]

    if len(odds) and odds[0][1] > 1:
        evens.append((odds[0][0], odds[0][1] - 1))
        odds[0] = (odds[0][0], 1)

    evens.sort()

    p = list()
    for x, c in evens:
        for k in range(c // 2):
            p.append(x)

    if len(odds):
        print(''.join(p + [odds[0][0] for _ in range(odds[0][1])] + p[::-1]))
    else:
        print(''.join(p + p[::-1]))


def __starting_point():
    main()


__starting_point()

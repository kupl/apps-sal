from collections import Counter


def solve(n, xs):
    rxs = list(reversed(xs))
    length = len(xs)
    counter = {}
    for i, x in enumerate(xs):
        if x in counter:
            counter[x]['cnt'] += 1
            counter[x]['last'] = i
        else:
            counter[x] = {'cnt': 0, 'first': i, 'last': i}
    ts = sorted(list(counter.items()), key=lambda t: t[1]['cnt'], reverse=True)
    maxs = []
    mv = 0
    mr = float('inf')
    rkey = 0
    for t in ts:
        k, d = t
        r = d['last'] - d['first']
        if mv <= d['cnt'] and mr > r:
            mv = d['cnt']
            mr = r
            rkey = k
    return counter[rkey]['first'] + 1, counter[rkey]['last'] + 1


def getinput():
    def getints_line():
        return list(map(int, input().split(' ')))
    n = int(input())
    xs = getints_line()
    return n, xs


def test():
    assert solve(5, [1, 1, 2, 2, 1]) == (1, 5)
    assert solve(5, [1, 2, 2, 3, 1]) == (2, 3)
    assert solve(6, [1, 2, 2, 1, 1, 2]) == (1, 5)


def main():
    print(' '.join(map(str, solve(*getinput()))))


def __starting_point():
    main()


__starting_point()

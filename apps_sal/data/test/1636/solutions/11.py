from collections import deque


def ordering(s, ws):
    pbs = {}
    for p in sorted(s):
        pbs.setdefault(p[1] - p[0], deque()).append(p)

    o = []
    os = set()
    for w in ws:
        try:
            p = pbs[w].popleft()
        except (IndexError, KeyError):
            return None

        if ((p[0] > 0 and (p[0] - 1, p[1]) not in os)
                or (p[1] > 0 and (p[0], p[1] - 1) not in os)):
            return None

        o.append(p)
        os.add(p)

    return o


def pair(x, y):
    return x, y


def __starting_point():
    n = int(input())
    s = {pair(*list(map(int, input().split()))) for _ in range(n)}
    ws = tuple(map(int, input().split()))
    o = ordering(s, ws)
    if o:
        print('YES')
        for p in o:
            print('{} {}'.format(*p))
    else:
        print('NO')


__starting_point()

from collections import namedtuple
plan = namedtuple('plan', ['time', 'x', 'y'])


def main():
    with open(0) as f:
        N = int(f.readline())
        plans = []
        for _ in range(N):
            (t, x, y) = map(int, f.readline().split())
            plans.append(plan(t, x, y))
    current = plan(0, 0, 0)
    for p in plans:
        t = p.time - current.time
        way = abs(p.x - current.x) + abs(p.y - current.y)
        if t < way:
            print('No')
            return None
        if t - way & 1:
            print('No')
            return None
        current = p
    else:
        print('Yes')


main()

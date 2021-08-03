import sys


def __starting_point():
    n, m = [int(c) for c in input().split()]
    s = []
    d = []
    c = []
    studying = []
    for _ in range(m):
        x, y, z = [int(w) for w in input().split()]
        s.append(x)
        d.append(y)
        c.append(z)

    plan = []

    for i in range(1, n + 1):

        if i in s:
            indices = [k for k, x in enumerate(s) if x == i]
            for idx in indices:
                studying.append((d[idx], idx))
            studying.sort()

        # print(studying)
        if i in d:
            idx = d.index(i)
            if (i, idx) in studying:
                print(-1)
                return
            else:
                plan.append(m + 1)
        else:
            if not studying:
                plan.append(0)
                continue
            idx = studying[0][1]
            plan.append(idx + 1)
            c[idx] -= 1
            if c[idx] == 0:
                studying = studying[1:]

    for i in plan:
        print(i, end=' ')
    print()


__starting_point()

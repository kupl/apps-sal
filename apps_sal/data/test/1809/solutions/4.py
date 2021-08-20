import sys


def main():
    (n, m) = tuple([int(x) for x in input().split()])
    w = [int(x) for x in input().split()]
    b = [int(x) - 1 for x in input().split()]
    o = []
    for i in range(m):
        if len(o) == n:
            break
        if b[i] not in [x[0] for x in o]:
            o.append((b[i], w[b[i]]))
    s = 0
    for i in range(m):
        ind = [o[i][0] for i in range(len(o))].index(b[i])
        s += sum([o[i][1] for i in range(ind)])
        el = o.pop(ind)
        o.insert(0, el)
    print(s)


def __starting_point():
    main()


__starting_point()

def main():
    from collections import deque
    n, k, *td = list(map(int, open(0).read().split()))
    s = list(zip(*[iter(td)] * 2))
    t = sorted(s, key=lambda x: x[1], reverse=True)

    variety = set()
    base = 0
    duplicated = deque([])

    for x, y in t[:k]:
        base += y
        if x in variety:
            duplicated.append(y)
        else:
            variety.add(x)

    now = base + len(variety) ** 2

    nx = deque(t[k:])
    c = len(variety)
    tmp = now
    while c < k and nx:
        i, j = nx.popleft()
        if i in variety:
            continue

        d = duplicated.pop()
        dif = j - d + 2 * c + 1
        variety.add(i)
        tmp = max(tmp, now + dif)
        now += dif
        c += 1

    print(tmp)


def __starting_point():
    main()


__starting_point()

def solve(x):
    res = [(1, x)]
    if x != 1:
        res.append((x, 1))
    (index, a, b) = (1, 1, 0)
    while True:
        b += a
        index += 1
        a += index
        if a * index - b > x:
            break
        if (x + b) % a == 0:
            m = (x + b) // a
            res.append((index, m))
            if index != m:
                res.append((m, index))
    res.sort()
    print(len(res))
    for ares in res:
        print(ares[0], ares[1])


def __starting_point():
    x = int(input())
    solve(x)


__starting_point()

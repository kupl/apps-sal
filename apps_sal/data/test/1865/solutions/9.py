def solve(xs):
    oxs = xs[:]
    oxs.sort()
    res = []
    for i in range(len(xs)):
        if xs[i] != oxs[i]:
            j = i + 1
            while not(oxs[i] == xs[j] and xs[j] != oxs[j]):
                j += 1
            res.append([i, j])
            xs[i], xs[j] = xs[j], xs[i]

    return res


def __starting_point():
    input()
    xs = list(map(int, input().split()))
    ret = solve(xs)
    print(len(ret))
    if ret: print(
        "\n".join(
            "{0[0]} {0[1]}".format(swp) for swp in ret
        )
    )


__starting_point()

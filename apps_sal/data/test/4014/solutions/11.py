def solve(n, m, ss, dd, cc):

    date = [-1] * (n + 1)
    for j, d in enumerate(dd):
        date[d] = j
    start = [[] for _ in range(n + 1)]
    for j, d in enumerate(ss):
        start[d].append(j)
    preps = []
    for i in range(1, n + 1):
        if start[i]:
            preps += start[i]
        u = date[i]

        if u >= 0:
            j = u
            if cc[j] > 0:
                return -1
            date[i] = m + 1
        else:
            if not preps:
                date[i] = 0
            else:
                min_d = min(dd[j] for j in preps)
                for j in preps:
                    if dd[j] == min_d:
                        break
                date[i] = j + 1
                cc[j] -= 1
                if cc[j] == 0:
                    preps.remove(j)

    return date[1:]


def main():
    n, m = [int(_) for _ in input().split()]

    s = []
    d = []
    c = []
    for i in range(m):
        s_, d_, c_ = [int(_) for _ in input().split()]

        s.append(s_)
        d.append(d_)
        c.append(c_)

    plan = solve(n, m, s, d, c)
    if isinstance(plan, list):
        print(' '.join(map(str, plan)))
    else:
        print(-1)


def __starting_point():
    main()


__starting_point()

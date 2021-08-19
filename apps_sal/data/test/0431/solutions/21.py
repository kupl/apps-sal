import sys

inf = float('inf')
ans = inf


def solve():
    n, m = map(int, input().split())
    s = [None] * n
    for i in range(n - 1, -1, -1):
        s[i] = [int(j) for j in input()]

    e = [any(si) for si in s]
    es = e[:] + [False]

    for i in range(n - 1, -1, -1):
        es[i] |= es[i + 1]

    # print(es)

    if not es[0]:
        print(0)
    elif es[0] and (not es[1]):
        k = -1

        for j in range(m, 0, -1):
            if s[0][j]:
                k = j
                break

        print(k)
    else:
        lim = 0

        for i in range(n + 1):
            if not es[i]:
                lim = i - 1
                break

        if not e[0]:
            left = 0
            right = m + 1
        else:
            for j in range(m, 0, -1):
                if s[0][j]:
                    kr = j
                    break

            left = 2 * kr
            right = m + 1

        # print(left, right)

        for i in range(1, lim):
            if not e[i]:
                left, right = min(left + 1, right + m + 2), min(right + 1, left + m + 2)
            else:
                kr = kl = -1

                for j in range(m, 0, -1):
                    if s[i][j]:
                        kr = j
                        break

                for j in range(1, m + 1):
                    if s[i][j]:
                        kl = j
                        break

                left, right = min(left + 1 + 2 * kr, right + m + 2), min(right + 1 + 2 * (m + 1 - kl), left + m + 2)

            # print(left, right)

        kr = kl = -1

        for j in range(m, 0, -1):
            if s[lim][j]:
                kr = j
                break

        for j in range(1, m + 1):
            if s[lim][j]:
                kl = j
                break

        ans = min(left + 1 + kr, right + 1 + m + 1 - kl)

        print(ans)


def __starting_point():
    solve()


__starting_point()

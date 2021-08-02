import sys
from itertools import accumulate


def solve():
    n, k = map(int, input().split())
    a = [int(i) for i in input().split()]

    ps = [0] + list(accumulate(a))
    ap = {ps[n]: 1}
    ans = 0

    if k == 1:
        for i in range(n - 1, -1, -1):
            if ps[i] + 1 in ap:
                ans += ap[ps[i] + 1]

            if ps[i] in ap:
                ap[ps[i]] += 1
            else:
                ap[ps[i]] = 1
    elif k == -1:
        for i in range(n - 1, -1, -1):
            if ps[i] + 1 in ap:
                ans += ap[ps[i] + 1]
            if ps[i] - 1 in ap:
                ans += ap[ps[i] - 1]

            if ps[i] in ap:
                ap[ps[i]] += 1
            else:
                ap[ps[i]] = 1
    else:
        kp = [k**i for i in range(50)]

        for i in range(n - 1, -1, -1):
            for kpi in kp:
                if ps[i] + kpi in ap:
                    ans += ap[ps[i] + kpi]

            if ps[i] in ap:
                ap[ps[i]] += 1
            else:
                ap[ps[i]] = 1

    print(ans)


def __starting_point():
    solve()


__starting_point()

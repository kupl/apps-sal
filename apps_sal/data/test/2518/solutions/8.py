def main():
    from math import ceil
    from copy import deepcopy
    n, a, b, *k = list(map(int, open(0).read().split()))
    k.sort()

    def check(x):
        q = deepcopy(k)
        cnt = 0
        while q:
            p = q.pop() - x * b
            if p <= 0:
                break
            cnt += ceil(p / (a - b))

        return cnt <= x

    l = 0
    r = k[-1]
    m = (l + r) // 2
    while l + 1 < r:
        if check(m):
            r = m
        else:
            l = m
        m = (l + r) // 2

    print((m+1))


def __starting_point():
    main()

__starting_point()

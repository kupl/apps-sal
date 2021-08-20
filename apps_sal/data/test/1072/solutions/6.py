def issorted(l):
    return all((l[i] <= l[i + 1] for i in range(len(l) - 1)))


def mainX(n, m, t):
    ans = 0
    while not issorted(t):
        remove = -1
        for i in range(len(t) - 1):
            if t[i] > t[i + 1]:
                for j in range(len(t[i])):
                    if t[i][j] != t[i + 1][j]:
                        remove = j
                        break
            if remove != -1:
                print(i, remove)
                break
        t = [_t[:remove] + _t[remove + 1:] for _t in t]
        ans += 1
    print(ans)


def is_good(s):
    return all((s[i] <= s[i + 1] for i in range(len(s) - 1)))


def line_is_good(a, j):
    return all((a[i][j] <= a[i + 1][j] for i in range(len(a) - 1)))


def main5(n, m, a):
    if n <= 1 or m <= 0 or is_good(a):
        print(0)
        return
    bad = []
    for i in range(0, m):
        if line_is_good(a, i):
            continue
        s = [''.join([k for (b, k) in enumerate(x) if b not in bad]) for x in a]
        print(i, bad)
        if is_good(s):
            print(len(bad))
            return
        else:
            bad.append(i)
    print(m)


def main6(n, m, a):
    if n <= 1 or m <= 0 or is_good(a):
        print(0)
        return
    bad = []
    good = list(range(m))
    ans = 0
    while not is_good(a):
        remove = -1
    return
    for i in range(0, m):
        if line_is_good(a, i):
            continue
        bad.append(i)
        s = [''.join([k for (b, k) in enumerate(x) if b not in bad]) for x in a]
        if is_good(s):
            print(len(bad))
            return
    print(m)


def main(n, m, a):
    if n <= 1 or m <= 0 or is_good(a):
        print(0)
        return
    bad = []
    ans = 0
    while not is_good(a):
        remove = -1
        for i in range(n - 1):
            if a[i] > a[i + 1]:
                for j in range(len(a[i])):
                    if a[i][j] > a[i + 1][j]:
                        remove = j
                        break
            if remove != -1:
                break
        a = [x[:remove] + x[remove + 1:] for x in a]
        ans += 1
    print(ans)


def main_input():
    (n, m) = [int(i) for i in input().split()]
    a = [input() for s in range(n)]
    main(n, m, a)


def __starting_point():
    main_input()


__starting_point()

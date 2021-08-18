

def solve(n, m, a):

    ans = 0
    s = [(a[0], 0)]
    for i in range(1, n):
        ans += (a[i] - a[i - 1]) % m
        s.append((a[i], i))
    s.sort()

    r = [0] * (m + 1)
    c = 0
    t = 0
    active = [0] * n
    j = 0
    while j < n:
        aj, _ = s[j]
        r[aj] += (aj * c - t - c)
        while j < n:
            ai, i = s[j]
            if ai != aj:
                break
            if 0 < i:
                if active[i - 1]:
                    active[i - 1] = 0
                    c -= 1
                    t -= a[i - 1]
            if i < n - 1:
                active[i] = 1
                c += 1
                t += a[i]
            j += 1

    if 0 < c:
        t -= m * c
        j = 0
        while j < n:
            aj, _ = s[j]
            r[aj] += (aj * c - t - c)
            while j < n:
                ai, i = s[j]
                if ai != aj:
                    break
                if 0 < i:
                    if active[i - 1]:
                        active[i - 1] = 0
                        c -= 1
                        t -= a[i - 1] - m
                j += 1
            if c == 0:
                break

    ans -= max(r)

    return ans


def main():
    n, m = input().split()
    n = int(n)
    m = int(m)
    a = list(map(int, input().split()))

    print((solve(n, m, a)))


def __starting_point():
    main()


__starting_point()

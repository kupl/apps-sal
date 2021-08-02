def main():
    N, A, B = list(map(int, input().split()))
    v = list(map(int, input().split()))
    v.sort(reverse=True)
    Amxv = sum(v[:A])
    c = v[A - 1]
    m = v[:A].count(c)
    n = v.count(c)
    fl = [1] * (N + 1)
    for i in range(N):
        fl[i + 1] = fl[i] * (i + 1)
    print((Amxv / A))
    if v[0] - c == 0:
        print((sum([fl[n] // (fl[i] * fl[n - i]) for i in range(A, min(B, n) + 1)])))
    else:
        print((fl[n] // (fl[m] * fl[n - m])))


def __starting_point():
    main()


__starting_point()

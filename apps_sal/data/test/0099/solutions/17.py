def solve():
    (b1, q, L, m) = map(int, input().split())
    a = set((int(i) for i in input().split()))
    if abs(b1) > L:
        print(0)
        return
    if b1 == 0:
        print(0 if b1 in a else 'inf')
        return
    if q == 0:
        if 0 in a:
            print(0 if b1 in a else 1)
        else:
            print('inf')
        return
    if q == 1:
        print(0 if b1 in a else 'inf')
        return
    if q == -1:
        print(0 if b1 in a and -b1 in a else 'inf')
        return
    b = b1
    ans = 0
    while abs(b) <= L:
        if b not in a:
            ans += 1
        b *= q
    print(ans)


def __starting_point():
    solve()


__starting_point()

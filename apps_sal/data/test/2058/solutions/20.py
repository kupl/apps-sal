def solve():
    S = input()
    T = input()

    lens = len(S)
    lent = len(T)

    a0 = [0] * lens
    a1 = [0] * lens
    for i in range(lens):
        if i > 0:
            a0[i] = a0[i - 1]
            a1[i] = a1[i - 1]
        if S[i] == '0':
            a1[i] += 1
        else:
            a0[i] += 1

    ans = 0
    for i in range(lens):
        if T[i] == '0':
            ans += a0[i]
        else:
            ans += a1[i]

    for i in range(lens, lent):
        if T[i] == '0':
            ans += a0[-1]
        else:
            ans += a1[-1]

    for i in range(lent - lens + 1, lent):
        d = lent - i
        if T[i] == '0':
            ans -= a0[-d - 1]
        else:
            ans -= a1[-d - 1]

    print(ans)


def __starting_point():
    solve()


__starting_point()

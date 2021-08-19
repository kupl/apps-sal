def main():
    (N, K) = list(map(int, input().split()))
    (R, S, P) = list(map(int, input().split()))
    T = input()
    ans = 0
    U = []
    for (i, t) in enumerate(T):
        if t == 'r':
            if i - K >= 0:
                if U[i - K] == 'p':
                    U.append('rs')
                    continue
            U.append('p')
            ans += P
        elif t == 's':
            if i - K >= 0:
                if U[i - K] == 'r':
                    U.append('sp')
                    continue
            U.append('r')
            ans += R
        else:
            if i - K >= 0:
                if U[i - K] == 's':
                    U.append('rp')
                    continue
            U.append('s')
            ans += S
    print(ans)


def __starting_point():
    main()


__starting_point()

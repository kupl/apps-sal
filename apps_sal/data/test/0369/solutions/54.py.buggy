def main():
    N, M = list(map(int, input().split()))
    *G, = list(map(int, input()))

    ans = []
    cur = N
    ecur = cur - 1
    while cur > 0:
        ncur = cur
        while (cur - ecur) <= M and ecur >= 0:
            if G[ecur] == 0:
                ncur = ecur
            ecur -= 1

        if ncur == cur:
            print((-1))
            return

        ans.append(cur - ncur)
        cur = ncur

    ans.reverse()

    print((*ans))


def __starting_point():
    main()


__starting_point()

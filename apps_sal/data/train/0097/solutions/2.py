def main():
    TT = int(input())
    for _ in range(TT):
        w, t = input().strip().split(' ')
        w = list(w)

        sf = [len(w) - 1 for _ in range(len(w))]
        for i in range(len(w) - 2, -1, -1):
            if w[i] < w[sf[i + 1]]:
                sf[i] = i
            else:
                sf[i] = sf[i + 1]

        for i in range(len(w)):
            if sf[i] != i and w[sf[i]] != w[i]:
                w[i], w[sf[i]] = w[sf[i]], w[i]
                break
        w = ''.join(w)
        if w < t:
            print(w)
        else:
            print('---')


def __starting_point():
    main()


__starting_point()

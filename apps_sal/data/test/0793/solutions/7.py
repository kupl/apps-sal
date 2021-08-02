from functools import reduce

NNN = 10 ** 9 + 7


def main():
    N, M = [int(a) for a in input().split()]
    S = [int(a) for a in input().split()]
    T = [int(a) for a in input().split()]

    table = [0] * M

    for si in reversed(S):
        c = 0
        for i in reversed(list(range(M))):
            prev_score = table[i]
            if T[i] == si:
                table[i] = (table[i] + c + 1) % NNN
            c = (c + prev_score) % NNN

    s = 1
    for a in table:
        s = (s + a) % NNN
    print(s)


def __starting_point():
    main()


__starting_point()

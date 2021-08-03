def main():
    S = input()[::-1]
    d1 = 'dream'[::-1]
    d2 = 'dreamer'[::-1]
    e1 = 'erase'[::-1]
    e2 = 'eraser'[::-1]
    while len(S) > 0:
        if S[:5] == d1:
            S = S[5:]
        elif S[:7] == d2:
            S = S[7:]
        elif S[:5] == e1:
            S = S[5:]
        elif S[:6] == e2:
            S = S[6:]
        else:
            print('NO')
            return
    print('YES')


def __starting_point():
    main()


__starting_point()

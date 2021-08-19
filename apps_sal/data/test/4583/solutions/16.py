def main():
    S = list(input())
    (A, B, C, D) = list(map(int, S))
    if A + B + C + D == 7:
        print('{}+{}+{}+{}=7'.format(A, B, C, D))
        return
    if A + B + C - D == 7:
        print('{}+{}+{}-{}=7'.format(A, B, C, D))
        return
    if A + B - C + D == 7:
        print('{}+{}-{}+{}=7'.format(A, B, C, D))
        return
    if A + B - C - D == 7:
        print('{}+{}-{}-{}=7'.format(A, B, C, D))
        return
    if A - B + C + D == 7:
        print('{}-{}+{}+{}=7'.format(A, B, C, D))
        return
    if A - B + C - D == 7:
        print('{}-{}+{}-{}=7'.format(A, B, C, D))
        return
    if A - B - C + D == 7:
        print('{}-{}-{}+{}=7'.format(A, B, C, D))
        return
    if A - B - C - D == 7:
        print('{}-{}-{}-{}=7'.format(A, B, C, D))
        return


def __starting_point():
    main()


__starting_point()

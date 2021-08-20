def __starting_point():
    S = input()
    N = len(S)
    if S[0] == S[-1]:
        if N % 2 == 0:
            print('First')
        else:
            print('Second')
    elif N % 2 == 0:
        print('Second')
    else:
        print('First')


__starting_point()

def main():
    N = int(input())
    for _ in range(N):
        S = str(input())
        if S.endswith('po'):
            print('FILIPINO')
        elif S.endswith('desu') or S.endswith('masu'):
            print('JAPANESE')
        else:
            print('KOREAN')


def __starting_point():
    main()


__starting_point()

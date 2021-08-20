def main():
    S = list(input())
    K = int(input())
    for i in range(min(K, len(S))):
        if S[i] != '1':
            print(S[i])
            return
    print('1')
    return


def __starting_point():
    main()


__starting_point()

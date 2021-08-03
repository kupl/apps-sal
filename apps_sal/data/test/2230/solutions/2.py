def __starting_point():
    N = int(input())
    st = 1
    en = N * N
    for i in range(N):
        for j in range(N // 2):
            print(st, end=" ")
            st += 1
            print(en, end=" ")
            en -= 1
        print()


__starting_point()

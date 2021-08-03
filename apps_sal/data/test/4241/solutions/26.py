def main():

    S = input()
    T = input()

    min = len(T)

    for i in range(len(S) - len(T) + 1):
        cnt = 0
        desS = S[i:i + len(T)]

        for j in range(len(T)):
            if desS[j] == T[j]:
                cnt += 1

        if min > len(T) - cnt:
            min = len(T) - cnt

    print(min)


def __starting_point():
    main()


__starting_point()

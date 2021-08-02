def main():
    N = int(input())
    S, T = input().split()
    for i in range(N):
        print(S[i] + T[i], end="")
    print()


def __starting_point():
    main()


__starting_point()

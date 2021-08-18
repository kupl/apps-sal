
def main():
    n = int(input())
    S, T = input().split()
    print(*[s + t for s, t in zip(S, T)], sep="")


def __starting_point():
    main()


__starting_point()

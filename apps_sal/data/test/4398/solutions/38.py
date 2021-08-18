
def main():
    n = int(input())
    s, t = input().split()
    print(*[s[i] + t[i] for i in range(n)], sep="")


def __starting_point():
    main()


__starting_point()

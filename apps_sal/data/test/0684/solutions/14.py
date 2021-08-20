def main():
    (a, b, c, d) = list(map(int, input().split()))
    print(b, c, c)


def __starting_point():
    t = int(input())
    for i in range(t):
        main()


__starting_point()

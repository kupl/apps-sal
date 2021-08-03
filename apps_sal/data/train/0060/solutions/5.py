def main():
    a, b = list(map(int, input().split()))
    print(a + b - 2 * (a & b))


def __starting_point():
    t = int(input())
    for i in range(t):
        main()


__starting_point()

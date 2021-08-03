def main():
    n = int(input())
    a = list(map(int, input().split()))
    a = sorted(a)
    print(a[len(a) // 2] - a[len(a) // 2 - 1])


def __starting_point():
    t = int(input())
    for i in range(t):
        main()


__starting_point()

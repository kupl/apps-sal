
def main():
    x, y = list(map(int, input().split()))
    n = int(input())

    lst = [x, y, y - x, -x, -y, x - y]
    lst = list([a % 1000000007 for a in lst])

    print(lst[(n - 1) % len(lst)])


def __starting_point():
    main()


__starting_point()

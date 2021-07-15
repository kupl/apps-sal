def main():
    n = int(input())
    lst = sorted(list(map(int, input().split())))
    for i in range(n - 1, -1, -1):
        if lst[i] <= i + 1:
            print(i + 2)
            return
    print(1)


def __starting_point():
    t = int(input())
    for i in range(t):
        main()

__starting_point()

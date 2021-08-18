
def main():
    n = int(input())
    arr = [-1, -1, -1, -1, 1, -1, 1, -1, 2, 1, 2, -1]
    for i in range(n):
        a = int(input())
        if (a >= 12):
            print(a // 4 - a % 2)
        else:
            print(arr[a])


def __starting_point():
    main()


__starting_point()

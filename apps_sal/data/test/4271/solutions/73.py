def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    point = sum(b)
    for i in range(1, n):
        if a[i - 1] + 1 == a[i]:
            point += c[a[i - 1] - 1]
    print(point)


def __starting_point():
    main()


__starting_point()

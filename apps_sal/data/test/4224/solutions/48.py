def main():
    n = int(input())
    a_lst = list(map(int, input().split()))
    count = 0
    for i in range(n):
        a = a_lst[i]
        while a % 2 == 0:
            count += 1
            a //= 2
    print(count)


def __starting_point():
    main()


__starting_point()

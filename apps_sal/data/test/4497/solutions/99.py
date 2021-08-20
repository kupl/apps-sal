def LI():
    return list(map(int, input().split()))


def I():
    return map(int, input().split())


mod = 10 ** 9 + 7


def main():
    n = int(input())
    cnt = 1
    while n >= cnt:
        ans = cnt
        cnt *= 2
    print(ans)


def __starting_point():
    main()


__starting_point()

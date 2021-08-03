def __starting_point():
    #n, m = list(map(int, input().split()))
    #s = list(input().split())
    n = int(input())
    if n % 3 == 0:
        print(2 * (n // 3))
    else:
        print(2 * (n // 3) + 1)


__starting_point()

def __starting_point():
    n = int(input())
    data = list(map(int, input().split()))
    if 1 in data:
        print('-1')
    else:
        print(1)


__starting_point()

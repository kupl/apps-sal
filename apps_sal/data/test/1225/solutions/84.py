def main():
    h = int(input())
    cnt = 0
    while h > 0:
        h //= 2
        cnt += 1
    x = 0
    for i in range(cnt):
        x = x * 2 + 1
    print(x)


def __starting_point():
    main()


__starting_point()

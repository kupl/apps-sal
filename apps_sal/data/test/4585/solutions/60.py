def main():
    x = int(input())
    cnt = 0
    for i in range(x + 1):
        cnt += i
        if cnt >= x:
            print(i)
            return


def __starting_point():
    main()


__starting_point()

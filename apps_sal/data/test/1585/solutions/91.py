def main():
    (x, y) = list(map(int, input().split()))
    cnt = 1
    while True:
        x *= 2
        if x <= y:
            cnt += 1
        else:
            break
    print(cnt)


def __starting_point():
    main()


__starting_point()

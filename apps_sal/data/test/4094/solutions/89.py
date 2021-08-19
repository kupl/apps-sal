def main():
    k = int(input())
    li = 7
    if k % 2 == 0:
        print(-1)
        return
    for i in range(k):
        if li % k == 0:
            print(i + 1)
            break
        li = (li * 10 + 7) % k
    else:
        print(-1)


def __starting_point():
    main()


__starting_point()

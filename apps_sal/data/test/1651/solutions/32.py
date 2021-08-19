def main():
    (s, p) = map(int, input().split())
    n = 1
    flag = False
    while n ** 2 <= p:
        if p % n == 0 and n + p // n == s:
            flag = True
            break
        n += 1
    if flag:
        print('Yes')
    else:
        print('No')


def __starting_point():
    main()


__starting_point()

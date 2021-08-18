

def main():
    K = int(input())
    N = 50
    loop, remain = divmod(K, N)
    a = [N - 1 + loop + N - remain + 1 if i < remain else N - 1 + loop - remain for i in range(N)]
    print(N)
    print((*a))


def __starting_point():
    main()


__starting_point()

def main():
    (N, K) = list(map(int, input().split()))
    D = set(map(int, input().split()))
    numset = set(range(0, 10))
    d = numset.difference(D)
    for n in range(N, pow(10, 6) + 10):
        check = set(list(str(n)))
        ngflag = False
        for i in check:
            if int(i) in D:
                ngflag = True
                break
        if not ngflag:
            break
    print(n)


def __starting_point():
    main()


__starting_point()

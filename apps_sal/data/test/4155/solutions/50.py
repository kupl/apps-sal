def divide_and_conuer(ls):
    mi = ls.index(min(ls))
    res = ls[mi]
    if(ls[mi + 1:len(ls)] != list()):
        res += divide_and_conuer(ls[mi + 1:len(ls)]) - ls[mi]
    if(ls[0:mi] != list()):
        res += divide_and_conuer(ls[0:mi]) - ls[mi]
    return res


def main():
    n = int(input())
    a = list(map(int, input().split()))
    print((divide_and_conuer(a)))


def __starting_point():
    main()


__starting_point()

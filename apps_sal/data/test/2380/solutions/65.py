def integerCards(n, m, alist, bclist):
    count = 0
    alist.sort()
    bclist.sort(key=lambda x: x[1], reverse=True)
    for (b, c) in bclist:
        for _ in range(b):
            if alist[count] < c:
                alist[count] = c
                count += 1
            else:
                break
            if count == n:
                break
        if count == n:
            break
    return sum(alist)


def main():
    (n, m) = map(int, input().split())
    alist = list(map(int, input().split()))
    bclist = [list(map(int, input().split())) for i in range(m)]
    print(integerCards(n, m, alist, bclist))


def __starting_point():
    main()


__starting_point()

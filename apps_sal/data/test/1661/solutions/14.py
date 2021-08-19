def main():
    (n, m) = [int(x) for x in input().split()]
    g = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]
    count = 0
    for i in g:
        if i <= a[count]:
            count += 1
            if count == len(a):
                break
    print(count)


def __starting_point():
    main()


__starting_point()

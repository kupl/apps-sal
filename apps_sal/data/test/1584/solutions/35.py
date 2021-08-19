import bisect


def main():
    n = int(input())
    l_lst = list(map(int, input().split()))
    l_lst.sort()
    count = 0
    for i in range(n - 1):
        for j in range(i + 1, n):
            a = l_lst[i]
            b = l_lst[j]
            tmp = bisect.bisect_left(l_lst, a + b)
            tmp -= j + 1
            tmp = max(0, tmp)
            count += tmp
    print(count)


def __starting_point():
    main()


__starting_point()

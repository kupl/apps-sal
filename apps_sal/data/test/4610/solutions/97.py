def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    lst = {}

    for num in A:
        if num in lst:
            lst[num] += 1
        else:
            lst[num] = 1

    lst_sorted = sorted(lst.items(), key=lambda x: x[1])

    len_lst_sorted = len(lst_sorted)

    if len_lst_sorted <= K:
        print(0)
        return
    else:
        ans = 0
        for i in range(len_lst_sorted - K):
            ans += lst_sorted[i][1]
        print(ans)
        return


def __starting_point():
    main()


__starting_point()

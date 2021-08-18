def main():
    from bisect import bisect

    N = int(input())
    A = sorted([int(x) for x in input().split()])
    B = sorted([int(x) for x in input().split()])
    C = sorted([int(x) for x in input().split()])

    lst = [N - bisect(C, b) for b in B]
    lst = lst[::-1]
    tmp_lst = [lst[0]]
    for i in lst[1:]:
        tmp_lst.append(i + tmp_lst[-1])
    tmp_lst = tmp_lst[::-1]

    ans = 0
    for a in A:
        res = bisect(B, a)
        ans += tmp_lst[res] if res < N else 0
    print(ans)


def __starting_point():
    main()


__starting_point()

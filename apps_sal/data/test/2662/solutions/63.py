def bisect_right_reverse(a, x):
    '''
    reverseにソートされたlist aに対してxを挿入できるidxを返す。
    xが存在する場合には一番右側のidx+1となる。
    '''
    if a[0] < x:
        return 0
    if x <= a[-1]:
        return len(a)
    # 二分探索
    ok = len(a) - 1
    ng = 0
    while (abs(ok - ng) > 1):
        mid = (ok + ng) // 2
        if a[mid] < x:
            ok = mid
        else:
            ng = mid
    return ok


def main():
    N = int(input())
    ans = 1
    lis_min = [int(input())]
    for i in range(N - 1):
        a = int(input())
        index = bisect_right_reverse(lis_min, a)
        if index != len(lis_min):
            lis_min[index] = a
        else:
            ans += 1
            lis_min.append(a)
    print(ans)


def __starting_point():
    main()


__starting_point()

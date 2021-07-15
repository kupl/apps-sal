def __starting_point():

    n,m = list(map(int,input().split()))

    A = list(map(int,input().split()))
    get_A = sum(A) / (4 * m)

    ans = 0
    for i in A:
        if get_A > i:
            continue
        ans += 1
    if ans >= m:
        print("Yes")
    else:
        print("No")


__starting_point()

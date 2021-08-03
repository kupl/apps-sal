def main():
    n = int(input())
    inlis = list(map(int, input().split()))
    adic = dict()
    ans = 0

    for i in range(n):
        a = inlis[i]
        if a not in adic:
            adic[a] = 1
        else:
            adic[a] += 1
        if adic[a] > a:
            ans += 1

    for num in adic:
        if adic[num] < num:
            ans += adic[num]

    print(ans)


def __starting_point():
    main()


__starting_point()

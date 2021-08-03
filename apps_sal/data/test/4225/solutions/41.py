def __starting_point():

    a, b, c, k = list(map(int, input().split()))

    ans = 0
    if k >= a:
        k -= a
        ans += a
    else:
        ans += k
        print(ans)
        return

    if k >= b:
        k -= b
    else:
        print(ans)
        return

    if k >= c:
        ans += c * (-1)
    else:
        ans += k * (-1)

    print(ans)


__starting_point()

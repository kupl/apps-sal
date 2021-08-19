def __starting_point():
    (a, b) = map(int, input().split())
    ans = a
    while a // b > 0:
        ans += a // b
        a = a // b + a % b
    print(ans)


__starting_point()

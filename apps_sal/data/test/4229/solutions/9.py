def __starting_point():
    n = int(input())
    ans = 0
    for i in range(1, n + 1):
        if i % 3 == 0 or i % 5 == 0:
            pass
        else:
            ans += i
    print(ans)


__starting_point()

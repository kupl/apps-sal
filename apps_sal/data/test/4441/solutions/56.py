def __starting_point():
    n = int(input())

    if n == 1:
        print("Hello World")
    else:
        ans = 0
        for i in range(2):
            ans += int(input())
        print(ans)


__starting_point()

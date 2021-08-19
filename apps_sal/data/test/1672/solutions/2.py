def __starting_point():
    N = int(input())
    ans = 0
    last = ''
    while N > 0:
        inp = input()
        if inp != last:
            ans += 1
        last = inp
        N -= 1
    print(ans)


__starting_point()

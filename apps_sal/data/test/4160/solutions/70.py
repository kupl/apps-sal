def __starting_point():
    x = int(input())
    ans = 100
    cnt = 0
    while True:
        ans = ans + ans // 100
        if ans >= x:
            cnt += 1
            break
        cnt += 1
    print(cnt)


__starting_point()

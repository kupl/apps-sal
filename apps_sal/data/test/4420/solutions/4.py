for _ in range(int(input())):
    x, y, n = list(map(int, input().split()))
    ans = y
    dif = n - ans
    dif %= x
    ans = n - dif
    print(ans)


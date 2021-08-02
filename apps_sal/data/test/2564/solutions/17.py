for _ in range(int(input())):
    a, b, n = map(int, input().split())
    cnt = 0
    while a <= n or b <= n:
        if a > b:
            b += a
        else:
            a += b
        cnt += 1
    print(cnt - 1)

for _ in range(int(input())):
    (n, x) = list(map(int, input().split()))
    l = 1
    r = 2
    cnt = 1
    while True:
        if l <= n <= r:
            print(cnt)
            break
        else:
            cnt += 1
            l = r + 1
            r += x

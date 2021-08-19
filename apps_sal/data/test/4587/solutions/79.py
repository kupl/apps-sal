def abc077c_snuke_festival():
    import bisect
    n = int(input())
    a = sorted(list(map(int, input().split())))
    b = sorted(list(map(int, input().split())))
    c = sorted(list(map(int, input().split())))
    total = 0
    for i in range(n):
        b_size = b[i]
        j = bisect.bisect_left(a, b_size)
        j = n - j
        k = bisect.bisect_right(c, b_size)
        total += (n - j) * (n - k)
    print(total)


abc077c_snuke_festival()

def __starting_point():
    (n, k) = list(map(int, input().split()))
    s = set()
    n = n % k
    while True:
        tmp = abs(n - k)
        if tmp in s:
            break
        s.add(tmp)
        n = min(n, tmp)
    print(n)


__starting_point()

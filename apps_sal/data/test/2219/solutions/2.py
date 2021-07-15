for TT in range(1, int(input()) + 1):
    n, k = map(int, input().split())
    res = 0
    while n:
        if n % k:
            res += n % k
            n -= n % k
        if n:
            n //= k
            res += 1
    print(res)

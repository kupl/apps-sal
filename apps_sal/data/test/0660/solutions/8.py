(n, b, p) = list(map(int, input().split()))
ansb = p * n
if n == 1:
    print(0, ansb)
else:
    k = 2
    while 2 * k <= n:
        k *= 2
    ansa = 0
    while n > 1:
        k //= 2
        ansa += b * 2 * k + k
        n -= k
        while 2 * k <= n:
            k *= 2
        while k > n:
            k //= 2
    print(ansa, ansb)

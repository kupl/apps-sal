(n, k, A, B) = (int(input()) for i in range(4))
if k == 1:
    print((n - 1) * A)
else:
    x = n
    ans = 0
    while x != 1:
        if 1 < x < k:
            ans += (x - 1) * A
            x = 1
        elif x % k != 0:
            ans += (x - x // k * k) * A
            x = x // k * k
        else:
            d = x - x // k
            ans += min(d * A, B)
            x //= k
    print(ans)

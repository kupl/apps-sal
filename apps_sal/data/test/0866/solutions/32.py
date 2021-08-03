X, Y = map(int, input().split())
if (X + Y) % 3 != 0:
    print(0)

else:
    # 経路
    def C(n, r, mod):
        num = 1
        den = 1
        for i in range(r):
            num *= n - i
            num %= mod
            den *= i + 1
            den %= mod
        return (num * pow(den, mod - 2, mod)) % mod
    mod = 10**9 + 7
    minimun = (X + Y) / 3
    if X >= minimun and Y >= minimun:
        X -= minimun
        Y -= minimun
        print(C(int(X + Y), int(X), mod))
    else:
        print(0)

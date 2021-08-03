A, B, X = list(map(int, input().split()))


def d(N):
    return len(str(N))


def price(N):
    return A * N + B * d(N)


def bisec(low, high):
    if low == high:
        return high
    elif low + 1 == high:
        if price(high) == X:
            return high
        else:
            return low
    else:
        n = (low + high) // 2
        if price(n) > X:
            return bisec(low, n)
        elif price(n) < X:
            return bisec(n, high)
        else:
            return n


if price(1) > X:
    print((0))
elif price(10**9) <= X:
    print((10**9))
else:
    print((bisec(1, 10**9)))

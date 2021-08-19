def sqr(x: int) -> int:
    return x * x


(a, b, c, d, e, f) = list(map(int, input().split()))
if a == b == c == d == e == f:
    print(sqr(a) * 6)
else:
    print(sqr(a + b + c) - sqr(a) - sqr(c) - sqr(e))

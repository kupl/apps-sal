n = int(input())


def sqrt(n):
    if n == 0:
        return 0
    x = 1 << (n.bit_length() + 1) // 2
    y = (x + n // x) // 2
    while y < x:
        x = y
        y = (x + n // x) // 2
    return x
# find a s.t. a(a+1)//2<=n+1


def f(n):
    # x**2+x-2(n+1)=0
    # -1+(1+8(n+1))
    return


print(n + 1 - (-1 + sqrt(1 + 8 * (n + 1))) // 2)

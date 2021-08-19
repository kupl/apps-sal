def f(b, e, m):
    result = 1
    while e != 0:
        if e & 1 == 1:
            result = result * b % m
        e >>= 1
        b = b * b % m
    return result


a = [int(i) for i in input().split()]
(n, m, k) = (a[0], a[1], a[2])
if k == -1:
    if (n + m) % 2 == 1:
        print(0)
    elif n == 1 or m == 1:
        print(1)
    else:
        print(f(2, n * m - n - m + 1, 1000000007))
elif k == 1:
    if n == 1 or m == 1:
        print(1)
    else:
        print(f(2, n * m - n - m + 1, 1000000007))

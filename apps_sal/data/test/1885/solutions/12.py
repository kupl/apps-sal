def fact(n):
    return 1 if n == 0 else n * fact(n - 1)


def c(n, k):
    return fact(n) // (fact(k) * fact(n - k))


n = int(input())
print(c(n, 5) + c(n, 6) + c(n, 7))

from math import factorial


def nCr(n, r):
    f = factorial
    return f(n) // f(r) // f(n - r)


n = int(input())
ans = nCr(n, 7) + nCr(n, 6) + nCr(n, 5)
print(ans)

def fac(n):
    if n == 0:
        return 1
    else:
        return n * fac(n - 1)


n = int(input())
m = n // 2
ans = fac(n) // (2 * m ** 2)
print(ans)

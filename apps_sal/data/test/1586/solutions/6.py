def func(n):
    if n % 2 == 1:
        return 0
    res = 0
    n //= 2
    while n:
        res += n // 5
        n //= 5
    return res


n = int(input())
print(func(n))

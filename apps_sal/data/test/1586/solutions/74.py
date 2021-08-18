n = int(input())
res = 0
if n % 2 == 0:
    for i in range(1, 30):
        p = n // (5 ** i)
        if p % 2 == 1:
            res += (p - 1) // 2
        else:
            res += p // 2
print(res)

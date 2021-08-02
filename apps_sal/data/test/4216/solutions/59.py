def divisor(n):
    i = 1
    f = 0
    table = []
    while i * i <= n:
        if n % i == 0:
            f = max(len(str(i)), len(str(n // i)))
            table.append(f)
        i += 1
    return table


n = int(input())
print((min(divisor(n))))

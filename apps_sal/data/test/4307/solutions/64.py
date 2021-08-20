def divisor(n):
    i = 1
    table = []
    while i * i <= n:
        if n % i == 0:
            table.append(i)
            table.append(n // i)
        i += 1
    table = list(set(table))
    return table


num = []
n = int(input())
for i in range(1, n + 1):
    if i % 2 != 0:
        if len(divisor(i)) == 8:
            num.append(i)
print(len(num))

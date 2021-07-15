def divisor(n):
    i = 1
    table = []
    while i * i <= n:
        if n % i == 0:
            table.append(i)
            table.append(n//i)
        i += 1
    table = list(set(table))
    return table


a, b, k = list(map(int, input().split()))
table = []
divisor_a = divisor(a)
divisor_b = divisor(b)
for i in divisor_a:
    if i in divisor_b:
        table.append(i)
table.sort(reverse=True)
print((table[k-1]))


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


(A, B, K) = map(int, input().split(' '))
a_divisor = divisor(A)
b_divisor = divisor(B)
print(sorted(list(set(a_divisor) & set(b_divisor)), reverse=True)[K - 1])

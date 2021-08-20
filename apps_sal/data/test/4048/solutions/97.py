def divisor(n):
    i = 1
    table = []
    while i * i <= n:
        if n % i == 0:
            table.append([i, n // i])
        i += 1
    return table


N = int(input())
m = N
if len(divisor(N)) == 1:
    print(N - 1)
else:
    for (i, j) in divisor(N):
        m = min(m, i + j)
    print(m - 2)

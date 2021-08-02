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


def resolve():
    n = int(input())
    ans = float('inf')
    c = divisor(n)
    for a in c:
        b = n // a
        ans = min(ans, a + b - 2)
    print(ans)


resolve()

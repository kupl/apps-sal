N = int(input())

cnt = []


def divisor(n):
    i = 1
    table = []
    while i * i <= n:
        if n % i == 0:
            table.append(i)
            table.append(n // i)
        i += 1
    table = list(set(table))
    if len(table) == 8:
        cnt.append(1)


for i in range(1, N + 1):
    if i % 2 != 0:
        divisor(i)

print(len(cnt))

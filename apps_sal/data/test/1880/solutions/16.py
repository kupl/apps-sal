n = int(input())
a1 = n // 10 ** 4
a2 = n // 10 ** 3 % 10
a3 = n // 10 ** 2 % 10
a4 = n // 10 % 10
a5 = n % 10
m = str((a1 * 10 ** 4 + a3 * 10 ** 3 + a5 * 10 ** 2 + a4 * 10 + a2) ** 5 % 100000)
m = '0' * (5 - len(m)) + m
print(m)

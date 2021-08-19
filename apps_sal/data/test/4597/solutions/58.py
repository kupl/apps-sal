n = int(input())
for i in range(n - 1):
    n *= i + 1
    n %= 10 ** 9 + 7
print(n)

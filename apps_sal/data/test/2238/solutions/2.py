n = int(input())
for i in range(n // 2 + 1):
    x = (n - (i * 2 + 1)) // 2
    print('*' * x + 'D' * (i * 2 + 1) + '*' * x)
for i in range(n // 2):
    x = (n - (n - i * 2 - 2)) // 2
    print('*' * x + 'D' * (n - i * 2 - 2) + '*' * x)

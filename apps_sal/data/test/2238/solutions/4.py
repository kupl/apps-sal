n = int(input())
for i in range(n):
    print('*' * abs(i - n // 2), end='')
    print('D' * (n - 2 * abs(i - n // 2)), end='')
    print('*' * abs(i - n // 2), end='')
    print()

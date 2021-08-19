a = int(input())
for i in range(a // 2):
    print('*' * (a // 2 - i), end='')
    print('D' * (i * 2 + 1), end='')
    print('*' * (a // 2 - i), end='')
    print()
for i in range(a // 2, -1, -1):
    print('*' * (a // 2 - i), end='')
    print('D' * (i * 2 + 1), end='')
    print('*' * (a // 2 - i), end='')
    print()

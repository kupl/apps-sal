n = int(input())
x = (n - 1) // 2
for i in range(x):
    print('*' * (x - i) + 'D' * (2 * i + 1) + '*' * (x - i))
print('D' * n)
for i in range(x):
    print('*' * (i + 1) + 'D' * (n - 2 * (i + 1)) + '*' * (i + 1))

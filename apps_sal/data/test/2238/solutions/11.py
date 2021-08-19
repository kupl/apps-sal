n = int(input())
k = 1
for i in range(n // 2, 0, -1):
    print('*' * i + 'D' * k + '*' * i)
    k += 2
print('D' * n)
k -= 2
for i in range(1, n // 2 + 1):
    print('*' * i + 'D' * k + '*' * i)
    k -= 2

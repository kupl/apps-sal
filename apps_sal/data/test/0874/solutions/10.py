n = int(input())
i = 0
if n // 2 == n / 2:
    while i < n:
        i = i + 2
        print(i, i - 1, end=' ')
else:
    print('-1')

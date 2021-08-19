n = int(input())
i1 = 1
for i in range(n):
    if i <= n // 2:
        for k in range((n - 2 * i - 1) // 2):
            print('*', end='')
        for l in range(2 * i + 1):
            print('D', end='')
        for m in range((n - 2 * i - 1) // 2):
            print('*', end='')
        print('\t')
    elif i == n // 2:
        for o in range(n):
            print('D', end='')
        print('\t')
    elif i > n // 2 and i < n:
        for p in range(i1):
            print('*', end='')
        for q in range(n - 2 * i1):
            print('D', end='')
        for r in range(i1):
            print('*', end='')
        i1 = i1 + 1
        print('\t')

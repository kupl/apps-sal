n = int(input())
for i in range(n):
    for j in range(n):
        if min(i, n - 1 - i) + min(j, n - 1 - j) < n // 2:
            print('*', end='')
        else:
            print('D', end='')
    print()

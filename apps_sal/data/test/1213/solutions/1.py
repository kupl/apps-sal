n, i = list(map(int, input().split()))
lozung = input()

if i > n // 2:
    while(i < n):
        print('RIGHT')
        i += 1
    while(i > 0):
        print('PRINT', lozung[i - 1])
        i -= 1
        if i != 0:
            print('LEFT')
else:
    while(i > 1):
        print('LEFT')
        i -= 1
    while(i <= n):
        print('PRINT', lozung[i - 1])
        i += 1
        if i != n + 1:
            print('RIGHT')

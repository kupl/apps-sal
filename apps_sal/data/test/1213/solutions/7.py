n, k = list(map(int, input().split()))
line = input()
if k <= n // 2:
    for i in range(k - 1):
        print('LEFT')
    print('PRINT', line[0])
    for i in range(n - 1):
        print('RIGHT')
        print('PRINT', line[i + 1])
else:
    for i in range(n - k):
        print('RIGHT')
    print('PRINT', line[-1])
    for i in range(n - 1):
        print('LEFT')
        print('PRINT', line[n - i - 2])

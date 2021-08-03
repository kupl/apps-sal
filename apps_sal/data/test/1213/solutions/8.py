[n, k], slogan = list(map(int, input().split())), input().strip()
if 2 * k < n + 1:
    for x in range(k - 2, -1, -1):
        print('LEFT')
        print('PRINT', slogan[x])
    for x in range(k - 1):
        print('RIGHT')
    print('PRINT', slogan[k - 1])
    for x in range(k, n):
        print('RIGHT')
        print('PRINT', slogan[x])
else:
    for x in range(k, n):
        print('RIGHT')
        print('PRINT', slogan[x])
    for x in range(n - k):
        print('LEFT')
    print('PRINT', slogan[k - 1])
    for x in range(k - 2, -1, -1):
        print('LEFT')
        print('PRINT', slogan[x])

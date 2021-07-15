n, k = map(int, input().split())
text = input().strip()

if k - 1 < n - k:
    for i in range(k - 1, 0, -1):
        print('LEFT')
    for i in range(n - 1):
        print('PRINT %s' % text[i])
        print('RIGHT')
    print('PRINT %s' % text[-1])
else:
    for i in range(k - 1, n - 1):
        print('RIGHT')
    for i in range(n - 1, 0, -1):
        print('PRINT %s' % text[i])
        print('LEFT')
    print('PRINT %s' % text[0])

(n, k) = list(map(int, input('').split()))
lozung = list(input())
if n - k < k:
    for i in range(k, n):
        print('RIGHT')
    for i in reversed(list(range(0, n))):
        print('PRINT ', lozung[i])
        if i != 0:
            print('LEFT')
else:
    for i in reversed(list(range(0, k - 1))):
        print('LEFT')
    for i in range(n):
        print('PRINT ', lozung[i])
        if i != n - 1:
            print('RIGHT')

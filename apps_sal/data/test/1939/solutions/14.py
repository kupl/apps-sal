(n, k) = [int(x) for x in input().split()]
for i in range(n):
    for j in range(n):
        if j != i:
            print('0', end=' ')
        else:
            print(str(k), end=' ')
    print('\n', end='')

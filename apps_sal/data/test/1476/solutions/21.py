n = int(input())
if n > 4:
    print(n)
    a = []
    for i in range(0, n, 2):
        a.append(i + 1)
    for i in range(1, n, 2):
        a.append(i + 1)
    for i in range(n - 1):
        print(a[i], end=' ')
    print(a[n - 1])
elif n < 3:
    print(1, 1, sep='\n')
elif n == 3:
    print(2, '1 3', sep='\n')
else:
    print(4, '3 1 4 2', sep='\n')

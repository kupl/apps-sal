t = int(input())
for i in range(t):
    n = int(input())
    a = [int(ii) for ii in input().split()]
    b = [0 for ii in range(n)]
    was = [0 for ii in range(n + 1)]
    minimum = 1
    for j in range(n):
        if j == 0 or a[j] != a[j - 1]:
            was[a[j]] = 1
            b[j] = a[j]
        else:
            while was[minimum] == 1:
                minimum += 1
            if minimum > a[j]:
                minimum = -1
                break
            b[j] = minimum
            was[minimum] = 1
    if minimum == -1:
        print(-1)
    else:
        for j in b:
            print(j, end=' ')
        print('')

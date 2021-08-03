def nod(a, b):
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return(a + b)


n, k = [int(i) for i in input().split()]
a = [0] * n
s = ''
if n <= k:
    print(-1)
else:
    for i in range(1, k + 1):
        a[i] = i + 1
    for i in range(k + 1, n - 1):
        a[i] = i + 2

    if n - k > 1:
        a[0] = k + 2
        a[n - 1] = 1
        a = [str(i) for i in a]
        print(' '.join(a))
    else:
        a[0] = 1
        a[n - 1] = n
        a = [str(i) for i in a]
        print(' '.join(a))

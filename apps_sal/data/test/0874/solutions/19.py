n = int(input())
if n % 2 == 1:
    print(-1)
else:
    a = ['0'] * n
    for i in range(n):
        a[i] = str(n - i)
    print(' '.join(a))

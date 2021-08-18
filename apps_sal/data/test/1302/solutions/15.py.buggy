n, k = map(int, input().split())
if(k > n - 1):
    print('-1')
    return

a = [0] * (n + 1)
for i in range(1, n + 1):
    a[i] = i
for i in range(n - k, 1, -1):
    a[i] = a[i - 1]
a[1] = n - k
for i in range(1, n + 1):
    if(i > 1):
        print(' ', end='')
    print(a[i], end='')
print('')

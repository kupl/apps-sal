n = int(input())
a = list(map(int, input().split()))
a.sort()
if a[n-1] < a[n-2] + a[n-3]:
    print('YES')
    print(' '.join(str(a[i]) for i in range(n - 2)) + ' ' + str(a[n-1]) + ' ' + str(a[n-2]))
else:
    print('NO')


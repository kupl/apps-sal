na, nb = list(map(int, input().split()))
k, m = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))
max = a[k - 1]
min = b[nb - m]
if max < min:
    print('YES')
else:
    print('NO')


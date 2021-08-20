(n, m) = list(map(int, input().split(' ')))
(k, l) = list(map(int, input().split(' ')))
a = input().split(' ')
b = input().split(' ')
for i in range(n):
    a[i] = int(a[i])
for i in range(m):
    b[i] = int(b[i])
if a[k - 1] < b[m - l]:
    print('YES')
else:
    print('NO')

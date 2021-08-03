n, x = map(int, input().split())
a = list(map(int, input().split()))
k = 0
for i in range(len(a) - 1):
    k += a[i] + 1
k += a[len(a) - 1]
if len(a) == 0 or k == x:
    print('YES')
else:
    print('NO')

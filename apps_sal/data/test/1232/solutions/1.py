(n, m) = map(int, input().split())
(k, p) = map(int, input().split())
x = 0
y = 0
a = input().split()
x = int(a[k - 1])
b = input().split()
y = int(b[m - p])
if x < y:
    print('YES')
else:
    print('NO')

(n, d) = list(map(int, input().split()))
m = int(input())
a = ['0'] * m
for i in range(m):
    (x, y) = list(map(int, input().split()))
    if y <= x + d and y >= x - d and (y >= -x + d) and (y <= 2 * n - d - x):
        a[i] = 'YES'
    else:
        a[i] = 'NO'
for x in a:
    print(x)

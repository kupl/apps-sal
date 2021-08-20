t = int(input())
for i in range(t):
    (a, b, c, n) = map(int, input().split())
    a = [a, b, c]
    a.sort()
    k = a[2] - a[1] + a[2] - a[0]
    if n < k:
        print('NO')
    elif (n - k) % 3 != 0:
        print('NO')
    else:
        print('YES')

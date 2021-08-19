(n, k, p, x, y) = map(int, input().split())
s = list(map(int, input().split()))
s = sorted(s)
if p < y:
    print(-1)
else:
    kol = 0
    summ = 0
    for i in s:
        summ += i
        if i >= y:
            kol += 1
    if k - kol >= n // 2 + 1 or summ > x:
        print(-1)
    elif kol >= n // 2 + 1:
        if summ + n - k <= x:
            print('1 ' * (n - k))
        else:
            print(-1)
    elif summ + y * (n // 2 + 1 - kol) + (n - k - n // 2 - 1 + kol) > x:
        print(-1)
    else:
        for i in range(n // 2 + 1 - kol):
            print(y, end=' ')
        for i in range(n - k - n // 2 - 1 + kol):
            print('1', end=' ')

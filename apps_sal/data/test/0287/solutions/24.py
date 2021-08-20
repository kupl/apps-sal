(n, k) = map(int, input().split())
if k == 0 or k == n:
    print('0 0')
else:
    mi = 1
    groups = n // 3
    if groups >= k:
        ma = 2 * k
    else:
        ma = n - k
    print(mi, ma)

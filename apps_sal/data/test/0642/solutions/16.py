(n, m) = map(int, input().split())
if m > 0:
    a = list(map(int, input().split()))
    a.sort()
    k = 0
    k1 = 1
    for i in range(1, m):
        if a[i] == a[i - 1] + 1:
            k1 += 1
        else:
            k = max(k, k1)
            k1 = 1
    k = max(k, k1)
    if k > 2 or (m >= 1 and (a[0] == 1 or a[-1] == n)):
        print('NO')
    else:
        print('YES')
else:
    print('YES')

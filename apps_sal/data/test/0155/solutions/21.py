n, m, k = map(int, input().split())
if k <= n - 1:
    print(1 + k, 1)
elif k <= n + m - 2:
    print(n, k - (n - 1) + 1)
else:
    k -= n - 1
    k -= m - 1
    #print('k', k)
    step = 1 + m - 2 + 1 + m - 2
    dy = k // (step // 2)
    y = n - dy
    if k % (step // 2):
        y -= 1
    k %= step
    if k == 0:
        x = m
    else:
        k -= 1
        if k <= m - 2:
            x = m - k
        else:
            k -= 1 + m - 2
            #print('k', k)
            x = 1 + k + 1
    print(y, x)

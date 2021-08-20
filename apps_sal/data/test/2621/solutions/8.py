def mp():
    return map(int, input().split())


t = int(input())
for tt in range(t):
    (n, m, k) = mp()
    a = list(mp())
    fail = False
    for i in range(n - 1):
        if a[i] >= a[i + 1]:
            m += min(a[i], a[i] - a[i + 1] + k)
        elif abs(a[i + 1] - a[i]) <= k:
            m += min(a[i], a[i] - a[i + 1] + k)
        elif m >= abs(a[i] - a[i + 1]) - k:
            m -= abs(a[i] - a[i + 1]) - k
        else:
            fail = True
            break
    if fail:
        print('NO')
    else:
        print('YES')

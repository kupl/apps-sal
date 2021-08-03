for _ in range(int(input())):
    n, m, k = list(map(int, input().split()))
    a = list(map(int, input().split()))
    ok = 1
    for i in range(n - 1):
        lo = max(0, a[i + 1] - k)
        if a[i] > lo:
            m += a[i] - lo
        else:
            m -= lo - a[i]
        if m < 0:
            ok = 0
            break
    print('YES' if ok else 'NO')

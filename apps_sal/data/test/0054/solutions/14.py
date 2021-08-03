def f(m, t):
    w = 0
    nonlocal n
    while n ** w * n < m:
        w += 1
    if n ** w * n == m or (m == 1 and t != 0):
        return True
    else:
        s1 = m - n ** w
        j = False
        k = False
        if w < t:
            j = f(abs(s1), w)
        if w + 1 < t:
            k = f(abs(n ** w * n - m), w + 1)
        if k == True or j == True:
            return True
        else:
            return False


n, m = list(map(int, input().split()))
if f(m, 101):
    print('YES')
else:
    print('NO')

def ans(m, n):
    (q1, q2, k) = (m, 2, 0)
    while q1 <= n:
        q1 *= 2
        k += q2
        q2 *= 2
    q2 //= 2
    q1 //= 2
    if n - q1 < q2:
        return k + n - q1 - q2 + 1
    return k


(n, k) = list(map(int, input().split()))
if k == n:
    print(1)
elif k == 1:
    print(n)
else:
    (l, r) = (1, n // 2 + 1)
    while r - l > 1:
        m = (l + r) // 2
        if ans(2 * m, n) >= k:
            l = m
        else:
            r = m
    (l1, r1) = (1, n // 2 + 1)
    while r1 - l1 > 1:
        m = (l1 + r1) // 2
        if ans(2 * m, n) >= k - 1:
            l1 = m
        else:
            r1 = m
    print(max(l1, 2 * l))

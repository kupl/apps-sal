def f(p, q, n):
    w = p
    r = 0
    while w <= n:
        r += n // w
        w *= p
    return r // q


(n, k) = list(map(int, input().split()))
i = 2
s = -1
while i * i <= k:
    if k % i == 0:
        cnt = 0
        while k % i == 0:
            k //= i
            cnt += 1
        j = f(i, cnt, n)
        if s < 0 or s > j:
            s = j
    i += 1
if k > 1:
    j = f(k, 1, n)
    if s > j or s < 0:
        s = j
print(s)

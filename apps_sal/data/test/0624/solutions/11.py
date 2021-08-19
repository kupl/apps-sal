(n, k, m) = list(map(int, input().split()))
a = sorted(map(int, input().split()))
res = 0
sm = sum(a)
for ai in a:
    if m < 0:
        break
    if m < k * n:
        alt = (sm + m) / n
    else:
        alt = sm / n + k
    res = max(res, alt)
    n -= 1
    m -= 1
    sm -= ai
print(res)

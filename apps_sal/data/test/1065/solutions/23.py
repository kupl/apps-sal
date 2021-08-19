def ifthen(x, y, z):
    return y if x else z


(n, k, M, D) = map(int, input().split())
t = M
t2 = n // M // k + ifthen(n // M % k, 1, 0)
ans = t * t2
for i in range(2, D + 1):
    l = n // (k * i)
    r = n // (k * (i - 1))
    tmp = k * (i - 1) + 1
    while r - l > 1:
        mid = (l + r) // 2
        if tmp * mid <= n:
            if mid <= M:
                ans = max(ans, mid * i)
            l = mid
        else:
            r = mid
    if tmp * l <= n and l <= M:
        ans = max(ans, l * i)
    if tmp * r <= n and r <= M:
        ans = max(ans, r * i)
print(ans)

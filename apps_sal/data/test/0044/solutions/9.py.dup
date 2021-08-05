d, k, a, b, t = map(int, input().split())

if d <= k:
    print(d * a)
elif t + k * a > k * b:
    print(k * a + (d - k) * b)
else:
    cnt = d // k
    s = k * a
    dd = d % k
    ans = (cnt * s) + ((cnt - 1) * t) + min(t + (dd * a), dd * b)
    print(ans)

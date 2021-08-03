from bisect import bisect_right as br
n, t = map(int, input().split())
a = list(map(int, input().split()))
ans = 0
l = min(a)
while t >= l:
    k = t
    m = 0
    for i in a:
        if k >= i:
            m += 1
            k -= i
    r = t // (t - k)
    ans += r * m
    t -= (t - k) * r
print(ans)

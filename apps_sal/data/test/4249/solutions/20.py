def check(d, a):
    ans = 0
    for q in range(len(a)):
        ans += max(a[q] - q // d, 0)
    return ans


n, m = list(map(int, input().split()))
a = sorted(list(map(int, input().split())), reverse=True)
if sum(a) < m:
    print(-1)
else:
    l, r = 0, n
    while r - l > 1:
        m1 = (l + r) // 2
        if check(m1, a) >= m:
            r = m1
        else:
            l = m1
    print(r)

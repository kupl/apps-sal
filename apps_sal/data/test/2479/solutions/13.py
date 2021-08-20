def f(i, m, cnt):
    while True:
        if i > n or not cnt[i] == inf:
            return
        cnt[i] = m
        i += 1


(n, q) = map(int, input().split())
inf = n + 114514
ans = (n - 2) * (n - 2)
(cnt1, cnt2) = ([inf] * (n + 1), [inf] * (n + 1))
(max1, max2) = (n - 2, n - 2)
for _ in range(q):
    (t, x) = map(int, input().split())
    if t == 1:
        if cnt1[x] == inf:
            ans -= max2
            max1 = x - 2
            f(x, max2, cnt1)
        else:
            ans -= cnt1[x]
    elif cnt2[x] == inf:
        ans -= max1
        max2 = x - 2
        f(x, max1, cnt2)
    else:
        ans -= cnt2[x]
print(ans)

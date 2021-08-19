(n, k) = list(map(int, input().split()))
a = list(map(int, input().split()))
ans = [min(i - 1, k) + 1 + min(n - i, k) for i in range(1, n + 1)]
for i in range(1, n + 1):
    a_ = a[i - 1]
    if a_ != 0:
        (l, r) = sorted([i, a_])
        d1 = ans[a_ - 1]
        d2 = max(0, l + 1 + min(n - l, k) - (r - min(r - 1, k)))
        delta = d1 - d2
        ans[i - 1] += delta
print(' '.join(map(str, ans)))

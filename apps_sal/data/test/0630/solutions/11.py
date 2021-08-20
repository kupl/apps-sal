(n, k) = map(int, input().split())
a = list(map(int, input().split()))
a = [i - 1 for i in a]
ans = []
for i in range(n):
    if a[i] == -1:
        ans.append(1 + min(n - i - 1, k) + min(i, k))
    else:
        ref = a[i]
        r1 = min(ref + k, n - 1)
        r2 = min(i + k, n - 1)
        l2 = max(i - k, 0)
        if l2 > r1:
            ans.append(ans[ref] + (r2 - l2 + 1))
        else:
            ans.append(ans[ref] + (r2 - r1))
print(' '.join([str(i) for i in ans]))

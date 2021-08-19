from bisect import bisect_left as lb
MOD = 10 ** 9 + 7
n = int(input())
a = [tuple(map(int, input().split())) for _ in range(n)]
a = sorted(((in_, out) for (out, in_) in a))
dp_suf = [None] * n
for i in range(n - 1, -1, -1):
    (in_, out) = a[i]
    j = lb(a, (out, 0))
    if j == n:
        (empty, count) = (in_, 1)
    else:
        (empty, count) = dp_suf[j]
        empty -= out - in_
    if i < n - 1:
        if empty > dp_suf[i + 1][0]:
            (empty, count) = dp_suf[i + 1]
        elif empty == dp_suf[i + 1][0]:
            count += dp_suf[i + 1][1]
    dp_suf[i] = (empty, count % MOD)
print(dp_suf[0][1])

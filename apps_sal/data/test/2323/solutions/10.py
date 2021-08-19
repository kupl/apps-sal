from bisect import bisect_left
n = int(input())
s = sorted((int(si) for si in input().split()))
ediff = sorted((x - s[i - 1] for (i, x) in enumerate(s) if i > 0))
cumsum = [0] * n
for i in range(n - 1):
    cumsum[i + 1] = cumsum[i] + ediff[i]
for _ in range(int(input())):
    (l, r) = map(int, input().split())
    ind = bisect_left(ediff, r - l + 1)
    print((r - l + 1) * (n - ind) + cumsum[ind], end=' ')

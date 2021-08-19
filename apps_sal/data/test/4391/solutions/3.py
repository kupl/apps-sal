from itertools import accumulate
(n, k) = list(map(int, input().split()))
a = list(map(int, input().split()))
acc = [0] + list(accumulate(a))
ans = 0
for i in range(n - k + 1):
    for j in range(i + k, n + 1):
        s = acc[j] - acc[i]
        t = s / (j - i)
        ans = max(t, ans)
print(ans)

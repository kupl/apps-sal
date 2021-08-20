from collections import defaultdict


def ii():
    return list(map(int, input().split()))


maxv = int(200000.0) + 1
(n, k) = ii()
cnt = defaultdict(int)
for a in ii():
    cnt[a] += 1
for i in range(maxv, -1, -1):
    cnt[i] += cnt[i + 1]
(cur, ans) = (0, 0)
i = maxv
while True:
    if cnt[i] == n:
        if cur:
            ans += 1
        break
    if cur + cnt[i] > k:
        ans += 1
        cur = 0
    cur += cnt[i]
    i -= 1
print(ans)

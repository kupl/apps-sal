import collections
(n, m) = map(int, input().split())
arr = [0] + list(map(int, input().split()))
cnt = collections.defaultdict(int)
cnt[0] += 1
for i in range(1, n + 1):
    arr[i] += arr[i - 1]
    arr[i] %= m
    cnt[arr[i]] += 1
ans = 0
for key in cnt.keys():
    ans += cnt[key] * (cnt[key] - 1) // 2
print(ans)

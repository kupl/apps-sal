import collections
n = int(input())
a = list(map(int, input().split()))
ans = 0
cnt = collections.defaultdict(int)
for i in range(n):
    ans += cnt[i - a[i]]
    cnt[i + a[i]] += 1
print(ans)

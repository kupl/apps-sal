from collections import defaultdict
(n, k) = map(int, input().split())
ar = [int(x) for x in input().split()]
first = [10000000000] * (n + 1)
last = [-1] * (n + 1)
for i in range(k):
    first[ar[i]] = min(first[ar[i]], i)
for i in range(k - 1, -1, -1):
    last[ar[i]] = max(last[ar[i]], i)
ans = 0
for i in range(1, n + 1):
    if last[i] == -1:
        ans += 1
    if i == n:
        continue
    if last[i] < first[i + 1]:
        ans += 1
    if last[i + 1] < first[i]:
        ans += 1
print(ans)

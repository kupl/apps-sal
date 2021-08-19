from collections import defaultdict
(n, k) = map(int, input().split())
lis = list(map(int, input().split()))
first = {}
last = defaultdict(int)
length = len(lis)
for i in range(length):
    if lis[i] not in first:
        first[lis[i]] = i
    last[lis[i]] = i
count = 0
for i in range(1, n + 1):
    if i not in first:
        if i == 1 or i == n:
            count += 2
        else:
            count += 3
        continue
    if i - 1 > 0 and first[i] >= last[i - 1]:
        count += 1
    if i + 1 <= n and first[i] >= last[i + 1]:
        count += 1
print(count)

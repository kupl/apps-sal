from collections import defaultdict
n, m = list(map(int, input().split()))
cnt = defaultdict(int)
for el in list(map(int, input().split())):
    cnt[el] += 1

res = float('inf')
for i in range(1, n+1):
    res = min(res, cnt[i])
print(res)


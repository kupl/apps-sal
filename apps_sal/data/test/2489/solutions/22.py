import collections

n = int(input())
arr = list(map(int, input().split()))
arr = sorted(arr)
s = set()
cnt = collections.Counter(arr)
for i in range(n):
    if arr[i] in s:
        continue
    if cnt[arr[i]] >= 2:
        s.add(arr[i])
    for j in range(2, 10**6 // arr[i] + 1):
        s.add(arr[i] * j)
ans = 0
for i in range(n):
    if arr[i] in s:
        continue
    ans += 1
print(ans)

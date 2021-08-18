import collections
n = int(input())
line = list(map(int, input().split()))
arr = sorted(line)
coll = collections.Counter(arr)
Ma = arr[-1]
s = set()
for i in range(n):
    if coll[arr[i]] >= 2:
        s.add(arr[i])
    for j in range(2, Ma // arr[i] + 1):
        s.add(arr[i] * j)
cnt = 0

for a in arr:
    if a in s:
        continue
    cnt += 1
print(cnt)

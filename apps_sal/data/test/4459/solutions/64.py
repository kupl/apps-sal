import collections
N = int(input())
lsA = list(map(int, input().split()))
counterA = collections.Counter(lsA)
ans = 0
for i in counterA.keys():
    if i == counterA[i]:
        continue
    if i < counterA[i]:
        ans += counterA[i] - i
    elif i > counterA[i]:
        ans += counterA[i]
print(ans)

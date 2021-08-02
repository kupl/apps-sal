import collections
n = int(input())
a = list(map(int, input().split()))
a = collections.Counter(a)
ans = 0
for i, j in list(a.items()):
    if i > j:
        ans += j
    else:
        ans += abs(i - j)
print(ans)

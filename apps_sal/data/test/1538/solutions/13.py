from bisect import *
n = int(input())
a = list(map(int, input().split()))
a.sort(reverse=True)
a = [-int(x) for x in a]
ans = 0
i = 0
while i < n:
    idx = bisect_right(a, a[i])
    ans = max(ans, idx - i)
    i = idx
print(ans)

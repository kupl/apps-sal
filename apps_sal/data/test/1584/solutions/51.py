n = int(input())
l = sorted(list(map(int, input().split())))
ans = 0
import bisect
for i in range(n-2):
    for j in range(i+1, n-1):
        ab = l[i]+l[j]
        idx = bisect.bisect_left(l, ab)
        ans += max(0, idx-j-1)
print(ans)

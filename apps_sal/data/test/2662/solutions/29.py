import bisect
import sys
readline = sys.stdin.readline

N = int(readline())
ans = []
for i in range(N):
    a = -int(readline())
    ind = bisect.bisect_right(ans, a)
    if ind == len(ans):
        ans.append(a)
    else:
        ans[ind] = a

print((len(ans)))

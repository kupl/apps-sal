import bisect
import sys
input = sys.stdin.readline
n, m, ta, tb, k = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a = [i + ta for i in a]

ans = 0
for i in range(n):
    cancel = k - i
    if cancel >= 0:
        if cancel + bisect.bisect_left(b, a[i]) >= m:
            ans = -1
            break
        else:
            ans = max(b[cancel + bisect.bisect_left(b, a[i])], ans)
    else:
        break

if k >= min(n, m):
    ans = -1

if ans == -1:
    print(-1)
else:
    print(ans + tb)

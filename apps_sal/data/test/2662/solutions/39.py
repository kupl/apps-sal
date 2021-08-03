from bisect import bisect_left
from collections import deque

n = int(input())
ans = []
ans.append(int(input()))
ans = deque(ans)
for i in range(n - 1):
    temp = int(input())
    if temp <= ans[0]:
        ans.appendleft(temp)
    else:
        ans[bisect_left(ans, temp) - 1] = temp
print((len(ans)))

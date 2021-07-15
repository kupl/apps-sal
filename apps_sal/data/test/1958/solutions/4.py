import collections
import math

n, p = map(int, input().split())
t = [input() for _ in range(n)]
t = t[::-1]
ans, apple = p // 2, 1
for i in range(1, n):
    if t[i] == 'halfplus':
        ans += apple * p + p // 2
        apple += apple + 1
    else:
        ans += apple * p
        apple *= 2
print(ans)

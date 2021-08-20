from collections import deque
n = int(input())
p = [int(x) for x in input().split()]
cur = n
ans = deque()
while cur > 1:
    ans.appendleft(str(cur))
    cur = p[cur - 2]
ans.appendleft('1')
print(' '.join(ans))

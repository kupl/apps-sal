from collections import deque
from itertools import count
Odd = deque(input())
Even = deque(input())
rtnList = lambda x: Odd if x & 1 else Even
ans = ''
for i in count(1, 1):
    try:
        s = rtnList(i).popleft()
    except IndexError:
        print(ans)
        return
    ans += s

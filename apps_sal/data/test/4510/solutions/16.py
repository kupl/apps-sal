import sys
from collections import deque, defaultdict
(n, k) = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))
dq = deque()
on_dq = defaultdict(int)
length = 0
for ele in a:
    if not on_dq[ele]:
        on_dq[ele] = 1
        length += 1
        dq.appendleft(ele)
        if length > k:
            item = dq.pop()
            on_dq[item] = 0
            length -= 1
print(length)
print(*dq)

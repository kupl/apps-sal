import sys
from typing import List
slist = input().split(',')
stack = [1 << 30]
res = [[]]
for s in slist:
    if s.isnumeric():
        stack.append(int(s))
        if len(stack) > len(res):
            res.append([])
    else:
        while stack[-1] == 0:
            stack.pop()
        stack[-1] -= 1
        res[len(stack) - 1].append(s)
while res[-1] == []:
    res.pop()
print(len(res))
for l in res:
    if l:
        print(*l)

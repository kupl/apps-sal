from collections import defaultdict
import sys

ss = []
for _ in range(int(sys.stdin.readline())):
    ss.append(sys.stdin.readline().strip())
lmap, rmap = defaultdict(int), defaultdict(int)

for s in ss:
    stack = []
    good = True
    for x in s:
        if x == '(':
            stack.append(x)
        else:
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                good = False
                break
    if good:
        lmap[len(stack)] += 1

    stack = []
    good = True
    for x in s[::-1]:
        if x == ')':
            stack.append(x)
        else:
            if stack and stack[-1] == ')':
                stack.pop()
            else:
                good = False
                break
    if good:
        rmap[len(stack)] += 1


res = 0
for val, cnt in list(lmap.items()):
    res += cnt * rmap[val]

print(res)

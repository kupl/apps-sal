from collections import deque

N = int(input())
S = input()
que = deque(S)
l = r = 0

for s in S:
    if s == '(':
        l += 1
    else:
        r += 1
    if l < r:
        que.appendleft('(')
        l += 1
else:
    ans = "".join(que)
    if r < l:
        ans = ans + ")" * (l - r)
print(ans)

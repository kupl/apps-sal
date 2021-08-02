# Thanks for mitribunskiy
# efficient input style
# https://codeforces.com/contest/1263/submission/66081769

from collections import deque
import sys
reader = (s.rstrip() for s in sys.stdin)
n = int(next(reader))
operations = next(reader)

left = deque()
right = deque()
cur = 0
max_n = n + 1
left.append((0, 0, 0, 0))
for i in range(max_n - 1):
    right.append((0, 0, 0, 0))

ans = [-1] * n
for i, c in enumerate(operations):
    if c == "R":
        cur += 1
        ci, _, _, _ = right.popleft()
        _, su, mi, ma = left[-1]
        left.append((-ci, su - ci, min(mi, su - ci), max(ma, su - ci)))
    elif c == "L":
        if cur:
            cur -= 1
            ci, _, _, _ = left.pop()
            _, su, mi, ma = right[0]
            right.appendleft((-ci, su - ci, min(mi, su - ci), max(ma, su - ci)))
    else:
        left.pop()
        q = 0
        if c == "(":
            q = 1
        elif c == ")":
            q = -1
        if left:
            ci, su, mi, ma = left[-1]
            left.append((q, su + q, min(mi, su + q), max(ma, su + q)))
        else:
            left.append((q, q, q, q))
    # check
    _, sl, mil, mal = left[-1]
    _, sr, mir, mar = right[0]
    if sl == sr and mil >= 0 and mir >= 0:
        ans[i] = max(mal, mar)
print(*ans)

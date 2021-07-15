def ii():
    return int(input())
def mi():
    return map(int, input().split())
def li():
    return list(mi())

n, k = mi()
a = li()

from collections import deque
q = deque(a)

c = q.popleft()
w = 0
while 1:
    x = q.popleft()
    if c > x:
        w += 1
        if w >= k or w >= n:
            ans = c
            break
        q.append(x)
    else:
        q.append(c)
        c = x
        w = 1
print(ans)

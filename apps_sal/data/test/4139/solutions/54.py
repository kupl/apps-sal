from collections import deque

n = int(input())
l = len(str(n))
ans = 0
q = deque([(0, 0, 0, 0, 0, 0)])
while q:
    a, b, c, d, e, f = q.pop()
    a = a*10 + b
    if a <= n and d >= 1 and e >= 1 and f >= 1:
        ans += 1
    if c == l:
        continue
    q.appendleft((a, 3, c+1, d+1, e, f))
    q.appendleft((a, 5, c+1, d, e+1, f))
    q.appendleft((a, 7, c+1, d, e, f+1))
print(ans)

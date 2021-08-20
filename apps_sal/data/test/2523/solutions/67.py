from collections import deque
(x, y) = (deque(), deque())
s = deque(list(input()))
n = len(s)
m = s[n // 2]
ans = (n + 1) // 2
for _ in range((n + 1) // 2):
    x.appendleft(s.popleft())
for _ in range(n // 2):
    y.appendleft(s.pop())
if n % 2 == 1:
    x.popleft()
for i in range(n // 2):
    if x[i] == y[i] == m:
        ans += 1
    else:
        break
print(ans)

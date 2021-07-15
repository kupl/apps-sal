from collections import deque
s = deque(input())
ans = ''
n = len(s)
if n % 2:
    c = 0
else:
    c = -1
for i in range(n):
    if c == 0:
        ans += s.popleft()
    else:
        ans += s.pop()
    c -= 1
    c %= 2
print(''.join(ans[::-1]))

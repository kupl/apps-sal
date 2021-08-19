from collections import deque
n = int(input())
s = list(input())
q = deque()
ans = n
for i in range(n):
    q.append(s[i])
    if len(q) <= 2:
        continue
    a = q.pop()
    b = q.pop()
    c = q.pop()
    if c + b + a == 'fox':
        ans -= 3
    else:
        q.append(c)
        q.append(b)
        q.append(a)
print(ans)

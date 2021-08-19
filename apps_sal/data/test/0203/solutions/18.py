from collections import deque
q = deque()
n = int(input())
s = input()
for let in s:
    q.append(let)
b = 0
while len(q) > 1 and abs(b) < 400000:
    c = q.popleft()
    if c == 'D':
        if b >= 0:
            q.append(c)
        b += 1
    if c == 'R':
        if b <= 0:
            q.append(c)
        b -= 1
print(q.pop())

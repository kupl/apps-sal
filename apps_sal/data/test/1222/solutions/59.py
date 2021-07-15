from collections import deque
k = int(input())
D = deque()
for i in range(1, 10):
    D.append(i)
 
for _ in range(k):
    d = D.popleft()
    r = d % 10
    if r != 0:
        D.append(d * 10 + r - 1)
    D.append(d * 10 + r)
    if r != 9:
        D.append(d * 10 + r + 1)
 
print(d)

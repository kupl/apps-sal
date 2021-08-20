from collections import deque
n = int(input())
line = list(input())
D = deque()
R = deque()
for i in range(n):
    if line[i] == 'D':
        D.append(i)
    else:
        R.append(i)
while D and R:
    d = D.popleft()
    r = R.popleft()
    if d < r:
        D.append(d + n)
    else:
        R.append(r + n)
if D:
    print('D')
else:
    print('R')

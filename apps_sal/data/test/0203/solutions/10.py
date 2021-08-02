from collections import deque

n = int(input())
s = input()
R, D = deque(), deque()

for num in range(n):
    if s[num] == 'D':
        D.append(num)
    else:
        R.append(num)

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

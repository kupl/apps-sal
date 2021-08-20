import collections
n = int(input())
s = input()
(R, D) = (collections.deque(), collections.deque())
for i in range(n):
    if s[i] == 'R':
        R.append(i)
    else:
        D.append(i)
while R and D:
    r = R.popleft()
    d = D.popleft()
    if r < d:
        R.append(n + r)
    else:
        D.append(n + d)
if D:
    print('D')
else:
    print('R')

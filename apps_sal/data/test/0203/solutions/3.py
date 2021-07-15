# Author: Maharshi Gor
from collections import deque
def read(t:type=int):
    return t(input())


def read_arr(t=int):
    return [t(i) for i in str(input()).split()]

D = deque()
R = deque()

k = read()
S = input()

n = len(S)

for i in range(len(S)):
    if S[i] == 'R':
        R.append(i)
    else:
        D.append(i)

while R and D:
    r = R.popleft()
    d = D.popleft()
    if r < d:
        R.append(r+n)
    else:
        D.append(d+n)

if R:
    print('R')
else:
    print('D')


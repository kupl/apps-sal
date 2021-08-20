from collections import deque
import sys
input = sys.stdin.readline
(N, M) = list(map(int, input().split()))
EIN = [0] * N
EOUT = [0] * N
EINLIST = [[] for i in range(N)]
EOUTLIST = [[] for i in range(N)]
for i in range(M):
    (x, y) = list(map(int, input().split()))
    x -= 1
    y -= 1
    EOUT[x] += 1
    EIN[y] += 1
    EOUTLIST[x].append(y)
    EINLIST[y].append(x)
Q = deque()
USE = [1] * N
for i in range(N):
    if EIN[i] == 0 or EOUT[i] == 0:
        Q.append(i)
        USE[i] = 0
while Q:
    x = Q.pop()
    for to in EOUTLIST[x]:
        if USE[to] == 0:
            continue
        EIN[to] -= 1
        if EIN[to] == 0:
            Q.append(to)
            USE[to] = 0
    for fr in EINLIST[x]:
        if USE[fr] == 0:
            continue
        EOUT[fr] -= 1
        if EOUT[fr] == 0:
            Q.append(fr)
            USE[fr] = 0


def loopfind():
    for i in range(N):
        if USE[i] == 1:
            break
    else:
        return []
    Q = deque()
    Q.append(i)
    USESET = {i}
    ANS = [i]
    while True:
        for to in EOUTLIST[ANS[-1]]:
            if USE[to] == 1:
                nextv = to
                break
        if nextv in USESET:
            break
        else:
            ANS.append(nextv)
            USESET.add(nextv)
    x = ANS.index(nextv)
    return ANS[x:]


def shortcut(ANS):
    ANSSET = set(ANS)
    LEN = len(ANS)
    flag = 0
    for i in range(LEN):
        for to in EOUTLIST[ANS[i]]:
            if to in ANSSET and ANS[(i + 1) % LEN] != to:
                flag = 1
                x = ANS.index(to)
                break
        if flag:
            break
    if flag:
        if x < i:
            return shortcut(ANS[x:i + 1])
        else:
            return shortcut(ANS[x:] + ANS[:i + 1])
    else:
        return ANS


ANS = shortcut(loopfind())
if len(ANS) == 0:
    print(-1)
else:
    print(len(ANS))
    for ans in ANS:
        print(ans + 1)

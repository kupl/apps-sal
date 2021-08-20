from collections import deque
import sys
input = sys.stdin.readline
n = int(input())
W = [input().strip() for i in range(n)]
V = {'a', 'i', 'u', 'e', 'o'}
K = []
for (i, w) in enumerate(W):
    count = 0
    VKEY = ''
    for word in w:
        if word in V:
            count += 1
            VKEY = word
    K.append([count, VKEY, i])
K.sort()
K2 = deque(K)
Q = deque()
Q2 = deque()
while K2:
    if len(K2) >= 2 and K2[0][0] == K2[1][0] and (K2[0][1] == K2[1][1]):
        x = K2.popleft()
        y = K2.popleft()
        Q2.append(x)
        Q2.append(y)
    else:
        x = K2.popleft()
        Q.append(x)
Q1 = deque()
while Q:
    if len(Q) >= 2 and Q[0][0] == Q[1][0]:
        x = Q.popleft()
        y = Q.popleft()
        Q1.append(x)
        Q1.append(y)
    else:
        x = Q.popleft()
ANS = []
while Q1 and Q2:
    x = Q1.popleft()
    y = Q2.popleft()
    z = Q1.popleft()
    w = Q2.popleft()
    ANS.append([x[2], y[2], z[2], w[2]])
while len(Q2) >= 4:
    x = Q2.popleft()
    y = Q2.popleft()
    z = Q2.popleft()
    w = Q2.popleft()
    ANS.append([x[2], z[2], y[2], w[2]])
print(len(ANS))
for (x, y, z, w) in ANS:
    print(W[x], W[y])
    print(W[z], W[w])

from collections import deque
import sys
input = sys.stdin.readline

t = int(input())

ESET = {"0", "2", "4", "6", "8"}


for test in range(t):

    n = input().strip()

    E = deque()
    O = deque()

    for s in n:
        if s in ESET:
            E.append(s)
        else:
            O.append(s)

    ANS = []
    while E and O:
        if E[0] < O[0]:
            x = E.popleft()
            ANS.append(x)
        else:
            x = O.popleft()
            ANS.append(x)

    if len(E) != 0:
        ANS.extend(E)
    elif len(O) != 0:
        ANS.extend(O)

    print("".join(ANS))

from collections import deque

S = input()
q = int(input())
Query = [list(map(str, input().split())) for _ in range(q)]

flg = True

D = deque(S)

for query in Query:
    if query[0] == "1":
        flg = not flg
    else:
        F, C = query[1], query[2]
        if (F == "1") and (flg is True):
            D.appendleft(C)
        elif (F == "1") and (flg is False):
            D.append(C)
        elif (F == "2") and (flg is True):
            D.append(C)
        elif (F == "2") and (flg is False):
            D.appendleft(C)

if flg:
    print("".join(D))
else:
    print("".join(list(reversed(D))))

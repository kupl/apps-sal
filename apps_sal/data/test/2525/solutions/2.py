from collections import deque

s = deque(input())
q = int(input())
flag = True

for _ in range(q):
    tfc = input().split()

    if tfc[0] == '1':
        if flag == True:
            flag = False
        else:
            flag = True
    else:
        if flag == True:
            if tfc[1] == '1':
                s.appendleft(tfc[2])
            else:
                s.append(tfc[2])
        else:
            if tfc[1] == '1':
                s.append(tfc[2])
            else:
                s.appendleft(tfc[2])

if flag == True:
    print(''.join(s))
else:
    s.reverse()
    print(''.join(s))

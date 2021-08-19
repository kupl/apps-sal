from collections import deque
s = deque(input())
q = int(input())
flag = 0
for _ in range(q):
    query = list(map(str, input().split()))
    if query[0] == '1':
        flag = 1 - flag
    elif query[1] == '1':
        if flag == 0:
            s.appendleft(query[2])
        else:
            s.append(query[2])
    elif flag == 0:
        s.append(query[2])
    else:
        s.appendleft(query[2])
if flag == 1:
    s.reverse()
print(*s, sep='')

from collections import deque
s = deque(list(input()))
q = int(input())
count = 0
for i in range(q):
    query = input()
    if query == '1':
        count += 1
    elif query[2] == '1':
        if count % 2 == 0:
            s.appendleft(query[-1])
        else:
            s.append(query[-1])
    elif count % 2 == 0:
        s.append(query[-1])
    else:
        s.appendleft(query[-1])
if count % 2 == 1:
    s.reverse()
print(*s, sep='')

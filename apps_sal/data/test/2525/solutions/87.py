from collections import deque
s = deque(input())
rev = 0
q = int(input())
for i in range(q):
    query = list(map(str, input().split()))
    if query[0] == '1':
        rev += 1
        rev %= 2
    else:
        (f, c) = query[1:]
        if f == '1':
            if rev:
                s.append(c)
            else:
                s.appendleft(c)
        elif rev:
            s.appendleft(c)
        else:
            s.append(c)
s = ''.join(s)
if rev:
    print(s[::-1])
else:
    print(s)

from collections import deque

s = deque(input())
q = int(input())

flag = True
for _ in range(q):
    temp = input().split()
    if len(temp) == 1:
        flag = not flag
    else:
        if flag:
            if temp[1] == "1":
                s.appendleft(temp[2])
            else:
                s.append(temp[2])
        else:
            if temp[1] == "1":
                s.append(temp[2])
            else:
                s.appendleft(temp[2])

if flag:
    print("".join(s))
else:
    print("".join(list(s)[::-1]))

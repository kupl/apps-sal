from collections import deque
d = deque(input())
q = int(input())
ans = 1
for i in range(q):
    a = input()
    if int(a[0]) == 1:
        ans = ans * (-1)
    else:
        if ans == 1:
            if int(a[2]) == 1:
                d.appendleft(a[4])
            else:
                d.append(a[4])
        else:
            if int(a[2]) == 1:
                d.append(a[4])
            else:
                d.appendleft(a[4])
if ans == 1:
    for i in range(len(d)):
        print(d[i], end="")
else:
    d.reverse()
    for i in range(len(d)):
        print(d[i], end="")

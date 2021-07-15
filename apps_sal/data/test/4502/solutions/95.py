from collections import deque
n = int(input())
a = list(map(int,input().split()))
b_1 = deque()
b_2 = deque()
switch = 0
for i in a:
    if switch == 0:
        b_1.append(i)
        b_2.appendleft(i)
        switch = 1
    else:
        b_2.append(i)
        b_1.appendleft(i)
        switch = 0
b_1 = list(b_1)
b_2 = list(b_2)
if switch == 0:
    print((' '.join(list(map(str,b_1)))))
else:
    print((' '.join(list(map(str,b_2)))))


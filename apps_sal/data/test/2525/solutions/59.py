from collections import deque
s = deque(list(input()))
n = int(input())
Q = []
for i in range(n):
    Q.append(list(input().split()))
count = 0
for q in Q:
    if q[0] == '1':
        count += 1
    elif q[0] == '2' and count % 2 == 0:
        if q[1] == '1':
            s.appendleft(q[2])
        else:
            s.append(q[2])
    elif q[1] == '1':
        s.append(q[2])
    else:
        s.appendleft(q[2])
ans = ''.join(s)
if count % 2 == 0:
    print(ans)
else:
    print(ans[::-1])

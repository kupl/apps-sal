from collections import deque
z = list(input())
Q = deque()
for i in z:
    Q.append(i)
q = int(input())
cnt = 0
for i in range(q):
    x = input()
    if x[0] == '1':
        cnt += 1
        cnt %= 2
    elif x[0] == '2':
        if x[2] == '1':
            if cnt % 2 == 0:
                Q.appendleft(x[4])
            else:
                Q.append(x[4])
        elif cnt % 2 == 0:
            Q.append(x[4])
        else:
            Q.appendleft(x[4])
if cnt % 2 == 1:
    Q.reverse()
print(''.join(Q))

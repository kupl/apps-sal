from collections import deque
d = deque(input())
n = int(input())
p = []
flg = 0
for i in range(n):
    p = list(input().split())
    if p[0] == '1':
        flg ^= 1
    elif p[1] == '1':
        if flg == 1:
            d.append(p[2])
        else:
            d.appendleft(p[2])
    elif flg == 1:
        d.appendleft(p[2])
    else:
        d.append(p[2])
if flg == 1:
    d.reverse()
a = ''
for i in d:
    a += i
print(a)

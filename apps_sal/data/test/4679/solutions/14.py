from collections import deque
s1 = str(input())
s2 = str(input())
s3 = str(input())
a = []
b = []
c = []
for i in range(len(s1)):
    a.append(s1[i])
for i in range(len(s2)):
    b.append(s2[i])
for i in range(len(s3)):
    c.append(s3[i])
a = deque(a)
b = deque(b)
c = deque(c)
x = a.popleft()
while True:
    if x == 'a':
        if len(a) == 0:
            print('A')
            break
        x = a.popleft()
    elif x == 'b':
        if len(b) == 0:
            print('B')
            break
        x = b.popleft()
    else:
        if len(c) == 0:
            print('C')
            break
        x = c.popleft()

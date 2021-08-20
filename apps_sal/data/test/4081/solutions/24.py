from collections import deque
n = int(input())
a = deque(list(map(int, input().split())))
b = []
d = []
if a[0] < a[-1]:
    b.append('L')
    d.append(a[0])
    a.popleft()
else:
    d.append(a[-1])
    a.pop()
    b.append('R')
while a:
    c = d[-1]
    if a[0] < a[-1]:
        if c < a[0]:
            d.append(a[0])
            a.popleft()
            b.append('L')
        elif c < a[-1]:
            d.append(a[-1])
            a.pop()
            b.append('R')
        else:
            break
    elif c < a[-1]:
        d.append(a[-1])
        a.pop()
        b.append('R')
    elif c < a[0]:
        d.append(a[0])
        a.popleft()
        b.append('L')
    else:
        break
print(len(b))
print(''.join(b))

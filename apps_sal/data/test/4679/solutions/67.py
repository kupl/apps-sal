from collections import deque
a = deque(reversed(input()))
b = deque(reversed(input()))
c = deque(reversed(input()))
ne = a.pop()
while(True):
    if ne == 'a':
        if not a:
            break
        ne = a.pop()
    elif ne == 'b':
        if not b:
            break
        ne = b.pop()
    else:
        if not c:
            break
        ne = c.pop()
print(ne.upper())

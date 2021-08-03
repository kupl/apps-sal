from collections import deque
d = deque()
for s in input():
    if s in d:
        print('no')
        return
    else:
        d.append(s)
print('yes')

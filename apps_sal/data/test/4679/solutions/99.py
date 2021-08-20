from collections import deque
A = deque(list(input()))
B = deque(list(input()))
C = deque(list(input()))
tern = 'a'
while True:
    if tern == 'a':
        if A:
            tern = A.popleft()
            continue
        win = 'A'
        break
    elif tern == 'b':
        if B:
            tern = B.popleft()
            continue
        win = 'B'
        break
    elif tern == 'c':
        if C:
            tern = C.popleft()
            continue
        win = 'C'
        break
print(win)

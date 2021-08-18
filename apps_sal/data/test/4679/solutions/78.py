from collections import deque
Sa = deque(input())
Sb = deque(input())
Sc = deque(input())

turn = 0
while True:
    if turn == 0:
        if len(Sa) == 0:
            ans = 'A'
            break
        tgt = Sa.popleft()
        if tgt == 'b':
            turn = 1
        elif tgt == 'c':
            turn = 2
    if turn == 1:
        if len(Sb) == 0:
            ans = 'B'
            break
        tgt = Sb.popleft()
        if tgt == 'a':
            turn = 0
        elif tgt == 'c':
            turn = 2
    if turn == 2:
        if len(Sc) == 0:
            ans = 'C'
            break
        tgt = Sc.popleft()
        if tgt == 'a':
            turn = 0
        elif tgt == 'b':
            turn = 1
print(ans)

import sys
from collections import deque as dq

h, w, P = [int(x) for x in input().split()]
S = [int(x) for x in input().split()]

board = []
for b in sys.stdin.read():
    for c in b:
        if c == '.':
            board.append(-1)
        elif 0 <= ord(c) - 49 <= 9:
            board.append(ord(c) - 49)
        elif c == '#':
            board.append(-2)

new_castles = [dq() for _ in range(P)]

for pos in range(h * w):
    if board[pos] >= 0:
        new_castles[board[pos]].append((pos, 0))

Q = dq()
player_Q = dq(p for p in range(P) if new_castles[p])
while player_Q:
    p = player_Q.popleft()
    Q = new_castles[p]
    # Do S[p] moves
    goal = Q[-1][1] + S[p]
    while Q and Q[0][1] != goal:
        pos, moves = Q.popleft()
        y = pos // w
        x = pos - y * w

        if 0 < x and board[pos - 1] == -1:
            board[pos - 1] = p
            Q.append((pos - 1, moves + 1))

        if x < w - 1 and board[pos + 1] == -1:
            board[pos + 1] = p
            Q.append((pos + 1, moves + 1))

        if 0 < y and board[pos - w] == -1:
            board[pos - w] = p
            Q.append((pos - w, moves + 1))

        if y < h - 1 and board[pos + w] == -1:
            board[pos + w] = p
            Q.append((pos + w, moves + 1))
    if Q:
        player_Q.append(p)

count = [0 for _ in range(P)]
for x in board:
    if x >= 0:
        count[x] += 1
print(*count)

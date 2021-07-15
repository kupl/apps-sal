import sys
from itertools import islice
from collections import deque
read = map(int, sys.stdin.read().split())

N = next(read)
A = [deque()] + [deque(islice(read, N - 1)) for _ in range(N)]
days = 1
available_players = deque(range(1, N + 1))
next_opponent = [0] * (N + 1)
played = set()

while available_players:
    player = available_players.popleft()
    if not A[player]:
        continue

    opponent = A[player].popleft()
    if next_opponent[opponent] == player:
        available_players.append(player)
        available_players.append(opponent)
        next_opponent[player] = 0
        next_opponent[opponent] = 0
        if player in played:
            days += 1
            played.clear()
        played.add(player)
        played.add(opponent)
    else:
        next_opponent[player] = opponent

for i in A:
    if len(i) > 0:
        print(-1)
        return
else:
    print(days)

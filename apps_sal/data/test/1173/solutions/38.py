N = int(input())
A = [None] * N

for i in range(N):
    A[i] = list(map(lambda x: int(x) - 1, input().split()))[::-1]


playable = set(range(N))

day = 0
while True:
    next_playable = set()
    done = set()
    for player in playable:
        if player in done:
            continue
        if len(A[player]) == 0:
            continue
        rival = A[player][-1]
        if rival in done:
            continue
        if len(A[rival]) == 0:
            continue
        if A[rival][-1] == player:
            done.add(player)
            done.add(rival)
            A[player].pop()
            A[rival].pop()
            next_playable.add(player)
            next_playable.add(rival)
    if len(next_playable) == 0:
        break
    playable = next_playable
    day += 1

ok = True
for i in range(len(A)):
    if len(A[i]) != 0:
        ok = False
        break

print((-1, day)[ok])

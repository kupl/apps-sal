n, needed = map(int, input().split())
players = list(map(int, input().split()))

winner = players[0]
wins = 0

for i in range(1, n):
    if players[i] > winner:
        winner = players[i]
        wins = 1
    else:
        wins += 1
    if wins >= needed:
        break
    
print(winner)

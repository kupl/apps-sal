n = int(input())
players = list(map(int, input().split()))
players.sort()
if players[n] > players[n - 1]:
    print('YES')
else:
    print('NO')

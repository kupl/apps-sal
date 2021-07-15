n = int(input())
games = list(input())

if games.count('A') > len(games) / 2:
    print('Anton')
elif games.count('A') < len(games) / 2:
    print('Danik')
else:
    print('Friendship')

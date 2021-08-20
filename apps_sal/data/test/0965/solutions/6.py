n = int(input())
players = input()
show_players = 0
index = players.find('I')
index2 = players[index + 1:].find('I')
if index2 == -1:
    if index == -1:
        print(players.count('A'))
    else:
        print(1)
else:
    print(0)

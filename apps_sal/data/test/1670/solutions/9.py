__author__ = 'Rakshak.R.Hegde'
teams = dict(h=input(), a=input())
n = int(input())
fouls = {}
while n:
    n -= 1
    details = input().split()
    player = details[1] + details[2]
    foulsByM = fouls.get(player, 0) + 1
    fouls[player] = foulsByM
    if details[3] == 'r' and foulsByM <= 2:
        fouls[player] = 3
        print(teams[details[1]], details[2], details[0])
    elif foulsByM == 2:
            print(teams[details[1]], details[2], details[0])

n = int(input())
countItems = 0

home = []
away = []

for x in range(n):
    team = input().split()
    home.append(int(team[0]))
    away.append(int(team[1]))

for x, y in enumerate(home):
    countItems += away.count(y)

print(countItems)

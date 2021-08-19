n = int(input())
countItems = 0
team_jersey = []
for x in range(n):
    team = input().split()
    team_jersey.append(int(team[0]))
    team_jersey.append(int(team[1]))
home = [team_jersey[x] for x in range(len(team_jersey)) if x % 2 == 0]
away = [team_jersey[x] for x in range(len(team_jersey)) if x % 2 != 0]
for (x, y) in enumerate(home):
    countItems += away.count(y)
print(countItems)

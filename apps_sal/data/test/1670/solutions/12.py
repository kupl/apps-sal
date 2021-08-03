teamname = []
teamname.append(input().strip())
teamname.append(input().strip())

n = int(input())
foul = [[0 for m in range(100)] for i in range(2)]

for i in range(n):
    info = input().split()
    t = int(info[0])
    team = info[1]
    m = int(info[2])
    card = info[3]

    if team == 'h':
        td = 0
    else:
        td = 1

    if foul[td][m] >= 2:
        continue
    if card == 'y':
        foul[td][m] += 1
    else:
        foul[td][m] += 2
    if foul[td][m] >= 2:
        print('{0} {1} {2}'.format(teamname[td], m, t))

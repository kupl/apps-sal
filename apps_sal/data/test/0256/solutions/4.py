team1, team2 = (lambda t : [[list(map(int, input().split())) for x in range(2)] for y in range(2)])('input')
if (lambda t1, t2 : any(all(t1[x][0] > t2[y][1] and t1[1 - x][1] > t2[1 - y][0] for y in range(2)) for x in range(2)))(team1, team2):
    print('Team 1')
elif (lambda t1, t2 : all(any(t2[y][0] > t1[x][1] and t2[1 - y][1] > t1[1 - x][0] for y in range(2)) for x in range(2)))(team1, team2):
    print('Team 2')
else:
    print('Draw')


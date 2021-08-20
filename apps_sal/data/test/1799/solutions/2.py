import heapq
n = int(input())
num_balloons = int(input().split()[0])
better_teams = []
current_place = 1
worse_teams = []
for i in range(1, n):
    inp = input().split()
    team_balloons = int(inp[0])
    team_size = int(inp[1])
    if team_balloons > num_balloons:
        current_place += 1
        better_teams.append(team_size - team_balloons + 1)
    else:
        worse_teams.append([team_balloons, team_size])
heapq.heapify(better_teams)
best_place = current_place
worse_teams = sorted(worse_teams, key=lambda x: -x[0])
ind = 0
while True:
    if len(better_teams) == 0:
        break
    removed_team = heapq.heappop(better_teams)
    num_balloons -= removed_team
    current_place -= 1
    if num_balloons < 0:
        break
    while ind < len(worse_teams) and worse_teams[ind][0] > num_balloons:
        heapq.heappush(better_teams, worse_teams[ind][1] - worse_teams[ind][0] + 1)
        current_place += 1
        ind += 1
    if current_place < best_place:
        best_place = current_place
print(best_place)

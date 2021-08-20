def make_tour(people):
    teams = []
    people.sort()
    for i in range(len(people)):
        if i % 2 == 0:
            teams.append([people[i]])
        else:
            teams[-1].append(people[i])
    return teams


(n, a, b) = map(int, input().split())
people = []
ind = 1
fl = True
for i in range(1, n + 1):
    people.append(i)
while True:
    teams = make_tour(people)
    if len(teams) == 1:
        break
    for i in range(len(teams)):
        if teams[i][0] == a and teams[i][1] == b or (teams[i][0] == b and teams[i][1] == a):
            fl = False
            print(ind)
            break
        elif teams[i][0] == a or teams[i][1] == a:
            teams[i] = [a]
        elif teams[i][0] == b or teams[i][1] == b:
            teams[i] = [b]
        else:
            teams[i] = [teams[i][0]]
    if not fl:
        break
    people = []
    for i in range(len(teams)):
        for j in range(len(teams[i])):
            people.append(teams[i][j])
    ind += 1
if fl:
    print('Final!')

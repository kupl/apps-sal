__author__ = 'Rakshak.R.Hegde'
n = int(input())
t = list(map(int, input().split()))
noOfTeams = min(t.count(1), t.count(2), t.count(3))
for (i, strength) in enumerate(t):
    t[i] = (i, strength)
ans = ''
for i in range(noOfTeams):
    team = []
    kind = 1
    while kind <= 3:
        for (index, val) in enumerate(t):
            if val[1] == kind:
                team.append(val[0])
                del t[index]
                kind += 1
                break
    for index in team:
        ans += str(index + 1) + ' '
    ans += '\n'
print(noOfTeams)
print(ans)

h = input()
a = input()
n = int(input())
t = []
team = []
m = []
card = []
visits = []
x = []
y = []
z = []


def alinput(x):
    x = x.split(' ')
    x[0] = int(x[0])
    x[2] = (x[2])
    t.append(x[0])
    if x[1] == 'a':
        x[1] = a
    else:
        x[1] = h
    team.append(x[1])
    m.append(x[2])
    card.append(x[3])
    return (t, m, team, card)


for i in range(0, n):
    alinput(x=input())


def check(i):
    for l in range(0, len(visits)):
        if(visits[l] == (m[i] + team[i])):
            return False
    return True


for i in range(0, n):
    if(check(i)):
        if card[i] == 'r':
            x.append(team[i])
            y.append(m[i])
            z.append(t[i])
            visits.append(m[i] + team[i])
        elif(card[i] == 'y'):
            for j in range(i + 1, n):
                if m[i] == m[j] and (team[i] == team[j]) and (card[j] == 'y'):
                    x.append(team[i])
                    y.append(m[i])
                    z.append(t[j])
                    visits.append(m[j] + team[j])
                    break

for i in range(0, len(x)):
    for j in range(i, len(x)):
        if(z[j] < z[i]):
            z[j], z[i] = z[i], z[j]
            x[j], x[i] = x[i], x[j]
            y[j], y[i] = y[i], y[j]

for i in range(0, len(x)):
    print(x[i] + ' ' + y[i] + ' ' + str(z[i]))

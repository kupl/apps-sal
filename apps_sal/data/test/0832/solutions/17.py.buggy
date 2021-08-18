n = int(input())

colors = []

teams = [x for x in range(n)]

res = 0

for i in range(n):
    colors.append(tuple(map(int, input().split())))


def calc(t, s):
    nonlocal colors
    res = 0
    if len(t) == 1:
        return 0
    for i in range(len(t)):
        if colors[t[0]][s] == colors[t[i]][1 - s]:
            res += 1
    return res + calc(t[1:], s)


print(calc(teams, 1) + calc(teams, 0))

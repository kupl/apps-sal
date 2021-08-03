n, k, x = map(int, input().split())
colors = list(map(int, input().split()))

groups = []

i = 0
while i < n:
    c = colors[i]
    nbC = 0
    while i < n and colors[i] == c:
        i += 1
        nbC += 1
    groups.append((c, nbC))

maxNbBallsDestroyed = 0
for i, group in enumerate(groups):
    if group[0] == x and group[1] >= 2:
        nbBallsDestroyed = group[1]
        past = i - 1
        future = i + 1
        while past >= 0 and future < len(groups) and groups[past][0] == groups[future][0] and groups[past][1] + groups[future][1] >= 3:
            nbBallsDestroyed += groups[past][1] + groups[future][1]
            past -= 1
            future += 1
        maxNbBallsDestroyed = max(maxNbBallsDestroyed, nbBallsDestroyed)

print(maxNbBallsDestroyed)

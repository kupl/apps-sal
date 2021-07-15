n = int(input())
nbColors = [0 for i in range(10**5 + 1)]
teamAway = []
for i in range(n):
	home, away = map(int, input().split())
	nbColors[home] += 1
	teamAway.append(away)

for away in teamAway:
	print(n - 1 + nbColors[away], n - 1 - nbColors[away])

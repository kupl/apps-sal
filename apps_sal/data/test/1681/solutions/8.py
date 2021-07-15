sheet = input()
garland = input()
sheetnum = dict()
garlandnum = dict()

for color in sheet:
	if not color in sheetnum:
		sheetnum[color] = 1
	else:
		sheetnum[color] = sheetnum[color] + 1

for color in garland:
	if not color in garlandnum:
		garlandnum[color] = 1
	else:
		garlandnum[color] = garlandnum[color] + 1

ans = 0
for color in list(garlandnum.keys()):
	if not color in sheetnum:
		ans = -1
		break
	if garlandnum[color] >= sheetnum[color]:
		ans = ans + sheetnum[color]
	else:
		ans = ans + garlandnum[color]

print(ans)
	
	



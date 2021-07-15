n = int(input())
profit = [int(x) for x in input().split(' ')]

daysInFolders = [0]
folders = 1
badDays = 0

for elem in profit:
	if elem < 0:
		if badDays >= 0 and badDays < 2:
			badDays += 1
			daysInFolders[-1] += 1
		elif badDays == 2:
			daysInFolders.append(1)
			folders += 1
			badDays = 1
		else:
			badDays += 1
			daysInFolders[-1] += 1
	else:
		daysInFolders[-1] += 1
		
print(folders)
print(' '.join([str(x) for x in daysInFolders]))


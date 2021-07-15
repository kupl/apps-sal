n,c = list(map(int,input().split(" ")))
nums = list(map(int,input().split(" ")))
# c is the target number
# number of c values seen
cPast = 0
countC = 0

for value in nums:
	if value == c:
		countC += 1

def sawC(groupsList):
	for key,groups in list(groupsList.items()):
		if groups[-1] < 0:
			groups[-1] -= 1
		else:
			groups += [-1]
	return groupsList

solution = countC
#other numbers, highest count stored in hash table
groupsList = {}
for num in nums:
	if num == c:
		groupsList = sawC(groupsList)
	elif num in list(groupsList.keys()):
		if groupsList[num][-1] > 0:
			groupsList[num][-1] += 1
		else:
			groupsList[num] += [1]
	else:
		groupsList[num] = [1]

for key,groups in list(groupsList.items()):
	# actually counting if good
	#print("groups: ",groups)
	maxDiff = 1
	currDiff = 0
	newDiff = 0
	for group in groups:
		currDiff += group
		if group > currDiff:
			currDiff = group
		if currDiff > maxDiff:
			maxDiff = currDiff
	if maxDiff + countC > solution:
		solution = countC + maxDiff
print(solution)
	
						
			









import time

debug = False

n1, m2 = list(map(int, input().split()))

tests = []
for i in range(n1):
	tests.append(list(input()))

if debug:
	print (tests)

begin = time.time()

if debug:
	print("---")

marks1 = []
result1 = []
for i in range(n1):
	marks1.append([i,0.0])
	result1.append(0)

marks2 = []
result2 = []
for j in range(m2):
	marks2.append([j,0.0])
	result2.append(0)

for i in range(n1):
	for j in range(m2):
		test = tests[i][j]
		if test == ">":
			marks1[i][1] += 1.0
		elif test == "<":
			marks2[j][1] += 1.0
		else:
			marks1[i][1] += 0.0001
			marks2[j][1] += 0.0001

marks1.sort(key=lambda val: val[1])
marks2.sort(key=lambda val: val[1])

if debug:
	print(marks1)
	print(marks2)

i = 0
j = 0
value = 0
lastmark = -1
lastItem = [0,0]

while i < n1 or j < m2:
	LetAdd = 0
	if i < n1 and j < m2:
		test = tests[marks1[i][0]][marks2[j][0]]
		if test == ">":
			LetAdd = 2
		else:
			LetAdd = 1
	elif i < n1:
		LetAdd = 1
	else:
		LetAdd = 2

	if LetAdd == 1:
		if marks1[i][1] != lastmark and lastItem[0] != 2 or lastItem[0] == 2 and tests[marks1[i][0]][lastItem[1]] != '=':
			if debug:
				if lastItem[0] == 2:
					print(1, lastmark, lastItem, marks1[i][0], tests[marks1[i][0]][lastItem[1]])
				else:
					print(1, lastmark, lastItem, marks1[i][0])
			value += 1
		lastmark = marks1[i][1]
		result1[marks1[i][0]] = value
		lastItem = [1,marks1[i][0]]
		i += 1
	else:
		if marks2[j][1] != lastmark and lastItem[0] != 1 or lastItem[0] == 1 and tests[lastItem[1]][marks2[j][0]] != '=':
			if debug:
				if lastItem[0] == 1:
					print(2, lastmark, lastItem, marks2[j][0], tests[lastItem[1]][marks2[j][0]])
				else:
					print(2, lastmark, lastItem, marks2[j][0])
			value += 1
		lastmark = marks2[j][1]
		result2[marks2[j][0]] = value
		lastItem = [2,marks2[j][0]]
		j += 1
	if debug:
		print("Set ", lastItem, " to ", value)

CheckCorrect = True
for i in range(n1):
	for j in range(m2):
		test = tests[i][j]
		if test == ">":
			if result1[i] <= result2[j]:
				CheckCorrect = False
		elif test == "<":
			if result1[i] >= result2[j]:
				CheckCorrect = False
		else:
			if result1[i] != result2[j]:
				CheckCorrect = False
if debug:
	print("---")

if debug:
	print("Time: ", time.time() - begin)

if CheckCorrect:
	print ("Yes")
else:
	print ("No")

if CheckCorrect or debug:
	print(*result1)
	print(*result2)


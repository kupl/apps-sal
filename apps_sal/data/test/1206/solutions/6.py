import sys
data = []
readIdx = 0
for line in sys.stdin.readlines():
	data += line.split()

def read():
	nonlocal readIdx
	readIdx += 1
	return data[readIdx - 1]

n, r, maxValue, power, mul = int(read()), 0, 0, 1, 1
froms, tos = [], []

def generate(i, maxIdx, secondMax, equal, ways):
	nonlocal n, r
	if i < n:
		for state in range(3):
			if state < 2:
				newWays = ways
				newEqual = equal
				if state == 0:
					newWays *= max(0, min(secondMax - 1, tos[i]) + 1 - froms[i])
				else:
					newEqual += 1
					newWays *= (froms[i] <= secondMax and tos[i] >= secondMax)
				if newWays > 0:
					generate(i + 1, maxIdx, secondMax, newEqual, newWays)
			elif maxIdx == None:
				greaterFrom = max(secondMax + 1, froms[i])
				greaterTo = tos[i]
				newWays = ways * max(0, greaterTo + 1 - greaterFrom)
				if newWays > 0:
					generate(i + 1, i, secondMax, equal, newWays)
	elif ways > 0 and ((maxIdx != None and equal > 0) or (maxIdx == None and equal >= 2)):
		r += ways * secondMax
		

for i in range(n):
	froms += [int(read())]
	tos += [int(read())]
	power *= 3
	maxValue = max(maxValue, tos[i])
	mul *= (tos[i] + 1 - froms[i])
for secondMax in range(maxValue + 1):
	generate(0, None, secondMax, 0, 1)
print(r / mul)


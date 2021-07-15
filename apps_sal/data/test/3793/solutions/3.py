import itertools
from itertools import permutations as perm
import copy

def getPerm(it, index):
	if index == 0:
		return it
	elif index == 1:
		return [it[0], it[2], it[1]]
	elif index == 2:
		return [it[1], it[0], it[2]]
	elif index == 3:
		return [it[1], it[2], it[0]]
	elif index == 4:
		return [it[2], it[0], it[1]]
	elif index == 5:
		return [it[2], it[1], it[0]]

def distance(coord1, coord2):
	return ((coord2[0] - coord1[0])**2 + (coord2[1] - coord1[1])**2 + (coord2[2] - coord1[2])**2)

dists = ([0]*6)*7

pointList =  [[int(x) for x in input().split()] for y in range(0, 8)]

p0 = pointList[0]

for x in range(0, 7):
	y = 0
	for pt in perm(pointList[x + 1], 3):
		# print(pt, p0)
		dists[x*6 + y] = distance(p0, pt)
		# print(dists)
		y += 1

# print(pointList)
# print(dists)
done = False
final = None

def same(it1, it2):
	# print(it1, it2)
	if list(it1) == list(it2):
		return True
	return False

def checkNotSame(indicesSoFar, newIndex):
	nonlocal pointList
	ptToComp = getPerm(pointList[len(indicesSoFar) + 1], newIndex)
	for c in range(len(indicesSoFar)):
		if same(getPerm(pointList[c + 1], indicesSoFar[c]), ptToComp):
			# print(getPerm(pointList[c + 1], indicesSoFar[c]), getPerm(pointList[len(indicesSoFar)], newIndex), False)
			return False
	return True



def checkCompatible(a, b):
	if a == b or a*2 == b or a == 2*b or a*3 == b or a ==3*b or 2*a == 3*b or 3*a== 2*b:
		return True
	return False

def getSeven(distList, soFar, index):
	nonlocal done
	nonlocal final
	if done == True:
		return
	if index == 7:
		# for h in range(0,7):
		# 	print(getPerm(pointList[h+1], soFar[h]), end=" ")
		# print()
		# for i in range(0,7):
		# 	print(dists[i*6+soFar[i]], end=" ")
		# print()
		# print(soFar)
		distsSoFar = [dists[i*6+soFar[i]] for i in range(0, 7)]
		# print(distsSoFar)
		lowest = min(distsSoFar)
		lows = 0
		twos = 0
		threes = 0
		for a in range(0, 7):
			if distsSoFar[a] == lowest:
				lows += 1
			elif distsSoFar[a] == lowest*2:
				twos += 1
			elif distsSoFar[a] == lowest*3:
				threes += 1
		if lows == 3 and twos == 3 and threes == 1:
			done = True
			final = soFar
		return
	for x in range(0, 6):
		if done == True:
			return
		if soFar == []:
			curList = copy.copy(soFar)
			curList.append(x)
			getSeven(distList, curList, index + 1)
		else:
			 # and checkNotSame(soFar, x)
			# print(getPerm(pointList[index], soFar[index - 1]), getPerm(pointList[index + 1], x))
			# print(distList[x+(index)*6], distList[soFar[index - 1]+(index - 1)*6])
			if checkCompatible(distList[x+(index)*6], distList[soFar[index - 1]+(index-1)*6]):
				if checkNotSame(soFar, x):
					# print("Enters")
					curList = copy.copy(soFar)
					curList.append(x)
					# print(curList)
					getSeven(distList, curList, index+1)
		# else:

getSeven(dists, [], 0)

if final is None:
	print("NO")
else:
	print("YES")
	print(p0[0], p0[1], p0[2])
	for b in range(0, 7):
		x, y, z = getPerm(pointList[b+1], final[b])
		print(x, y, z)







# print(combosList)


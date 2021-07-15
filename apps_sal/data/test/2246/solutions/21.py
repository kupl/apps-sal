class Node:
	def __init__(self, index):
		self.neighbours = []
		self.index = index
		self.prob = 1.0
		self.vis = False
		self.length = 0

	def addNode(self, city):
		self.neighbours.append(city)
		if self.index == 1:
			self.prob = 1.0 / len(self.neighbours)
		else:
			l = len(self.neighbours)
			self.prob = 1.0  if l < 2 else (1.0 / (l - 1))

n = int(input())
if n == 1:
	print(0)
	return
	
cities = {}

for i in range(n-1):
	a, b = [int(k) for k in input().split()]
	#print ("test ", a, " to ", b)
	if a not in cities:
		cities[a] = Node(a)
	cities[a].addNode(b)
	if b not in cities:
		cities[b] = Node(b)
	cities[b].addNode(a)

if len(cities) == 2:
	print(1)
	return


# for i in range(1, n + 1, 1):
# 	print ("city.index ", cities[i].index, ' roads ', cities[i].neighbours, ' prob ', cities[i].prob)


# deadends = []
# deadendsProb = []


# def Parse(city, prob, length, oldCity):
# 	#print ('parse ', city.index)
# 	newprob = 1.0 if oldCity == 0  else cities[oldCity].prob
# 	#print ('nnewProb ', newprob)
# 	prob *= newprob
# 	#print (city.index, ' len ', len(city.neighbours))
# 	if len(city.neighbours) == 1 and oldCity != 0:
# 		deadends.append(length)
# 		deadendsProb.append(prob)
# 	else:
# 		#print (city.neighbours)
# 		length += 1
# 		for c in city.neighbours:
# 			if c != oldCity:
# 				Parse(cities[c], prob, length, city.index )

# Parse(cities[1], 1.0, 0, 0)
# #for i in range(len(deadends)):
# #	print('len ', deadends[i], ' prob ', deadendsProb[i])

# ans = sum(map(lambda l, p: l * p, deadends, deadendsProb))
# #print('ans', ans)
# print(ans)


def inorder(city):
	s = []
	s.append(city)
	#print ('index ', city.index)
	#print ('neighbours ', city.neighbours)
	while s:
		city = s.pop()
		city.vis = True
		if city.neighbours:
			if city.index == 1 or len(city.neighbours) > 1:
				for c in city.neighbours:
					if not cities[c].vis:
						cities[c].length = city.length + 1
						cities[c].prob *= city.prob
						s.append(cities[c])
			else:
				yield (city.index, city.prob, city.length)



test = sum([city[1] * city[2] for city in inorder(cities[1])])
print(test)



# this is a tree


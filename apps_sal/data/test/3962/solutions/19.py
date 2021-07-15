n = int(input())
leftSpaces = []
rightSpaces = []
for i in range(n):
	left,right = map(int,input().split(" "))
	leftSpaces += [left]
	rightSpaces += [right]
leftSpaces.sort()
rightSpaces.sort()
chairs = 0
for i in range(n):
	chairs += 1
	chairs += max(leftSpaces[i],rightSpaces[i])
print(chairs)

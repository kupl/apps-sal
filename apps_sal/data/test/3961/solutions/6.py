#! python3
numRooms = int(input())
links = [0] + [int(x) for x in input().split()]
portalPaths = [0] * (numRooms + 2)
for index in range(1, numRooms + 1):
    portalPaths[index + 1] = (2 * portalPaths[index] - portalPaths[links[index]] + 2) % 1000000007
print(portalPaths[numRooms + 1] % 1000000007)

# print(numRooms)
# print(links)


# This implementation is too slow
# numRooms = int(input())
# links = [-1]+[int(x) for x in input().split()]
# crosses = [0]+[0]*(numRooms + 1)
# current = 1
# while current <= numRooms:
# 	if crosses[current] % 2 == 0:
# 		crosses[current] += 1
# 		print(current, crosses[current], "portal")
# 		current = links[current]
# 	else:
# 		crosses[current] += 1
# 		print(current, crosses[current], "plus 1")
# 		current += 1

# print(sum(crosses) % 1000000007)

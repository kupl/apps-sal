numRooms = int(input())
links = [0] + [int(x) for x in input().split()]
portalPaths = [0] * (numRooms + 2)
for index in range(1, numRooms + 1):
    portalPaths[index + 1] = (2 * portalPaths[index] - portalPaths[links[index]] + 2) % 1000000007
print(portalPaths[numRooms + 1] % 1000000007)

3

import sys
import math

n = int(sys.stdin.readline())
movement_array = [int(nbr) for nbr in sys.stdin.readline().split()]

relative_pos = [(0,1)]
currentPos = 0
direction = 1
for move in movement_array:
	currentPos += move * direction
	direction *= -1
	relative_pos.append((currentPos,direction))

objective_pos = []
#print(relative_pos)
minimum = min(relative_pos, key=lambda x: x[0])[0]
for n in range(0,len(relative_pos)):
	objective_pos.append((relative_pos[n][0] + (-minimum), relative_pos[n][1]))

width = 0
for n in range(0,len(objective_pos)-1):
	width += math.fabs(objective_pos[n+1][0]-objective_pos[n][0])
width = int(width)

height = max(objective_pos, key=lambda x: x[0])[0] + 1

matrix = [[" " for x in range(width)] for x in range(height-1)]

#print(objective_pos)
 
xpos = 0
for n in range(0,len(objective_pos)-1):
	direction = objective_pos[n][1]
	ypos = objective_pos[n][0]
	#print(ypos)
	targetpos = objective_pos[n+1][0]
	while math.fabs(ypos - targetpos) > 0:
		if direction == 1:
			matrix[ypos][xpos] = "/"
			ypos += 1
		else:
			matrix[ypos-1][xpos] = "\\"
			ypos -= 1
		xpos += 1

for row in reversed(matrix):
	print("".join(row))







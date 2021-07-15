def eq(cube, a,b,c,d):
	return cube[a] == cube[b] and cube[b] == cube[c] and cube[c] == cube[d]

opp = [2,5,0,4,3,1]
cube = input().strip().split()
for i in range(6):
	if cube[4*i + 0] == cube[4*i + 1] and cube[4*i + 2] == cube[4*i + 1] and cube[4*i + 2] == cube[4*i + 3]:
		if cube[4*opp[i] + 0] == cube[4*opp[i] + 1] and cube[4*opp[i] + 2] == cube[4*opp[i] + 1] and cube[4*opp[i] + 2] == cube[4*opp[i] + 3]:
			# face1 = 0
			# for j in range(6):
			# 	if j != i and j != opp[i]:
			# 		face = j
			# 		break
			# face2 = 0
			# for j in range(6):
			# 	if j != face1 and j != i and j != opp[face1] and j != opp[i]:
			# 		face2 = j
			# 		break
			if (i == 0 or i == opp[0]):
				if (cube[4] == cube[5] and cube[4] == cube[18] and cube[18] == cube[19]):
					if (cube[16] == cube[17] and cube[17] == cube[22] and cube[22] == cube[23]):
						if (cube[20] == cube[21] and cube[21] == cube[14] and cube[14] == cube[15]):
							print("YES")
							return
				if (cube[4] == cube[5] and cube[4] == cube[15] and cube[14] == cube[15]):
					if cube[12] == cube[13] and cube[12] == cube[23] and cube[22] == cube[23]:
						if (cube[20] == cube[21] and cube[18] == cube[19] and cube[20] == cube[18]):
							print("YES")
							return
			if (i == 1  or i == opp[1]):
				if (eq(cube,2,3,12,14)):
					if (eq(cube,13, 15, 10, 11)):
						if (eq(cube, 8,9,19,17)):
							print("YES")
							return
				if eq(cube,2,3,17,19) and eq(cube,16,18,10,11) and eq(cube,8,9,12,14):
					print("YES")
					return
			if (i == 3 or i == opp[3]):
				if eq(cube,4,6,1,3) and eq(cube,0,2,20,22) and eq(cube,21,23,9,11):
					print("YES")
					return
				if eq(cube,4,6,9,11) and eq(cube,8,10,20,22) and eq(cube,21,23,1,3):
					print("YES")
					return

print("NO")

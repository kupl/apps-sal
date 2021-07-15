p1 = list(map(int, input().split()))
p2 = list(map(int, input().split()))
p3 = list(map(int, input().split()))
p = [p1, p2, p3]
if (p1[0]==p2[0] and p2[0]==p3[0]) or (p1[1]==p2[1] and p2[1]==p3[1]):
	print(1)
else:
	for i in range(3):
		for j in range(3):
			for k in range(3):
				if (i != j) and (j!=k) and(i!=k):
					#print(i,j,k)
					for z in range(2):
						z2 = 1-z
						if (p[i][z] == p[j][z]) and not(min(p[i][z2],p[j][z2]) < p[k][z2] < max(p[i][z2],p[j][z2])):
							print(2)
							return
	print(3)


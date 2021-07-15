a = input().split()
a = [int(i) for i in a]
line1 = input().split()
line2 = input().split()
if line1[0] == '0':
	print ('NO')
else:
	if line1[a[1] - 1] == '1':
		print ('YES')
	else:
		done = False
		if line2[a[1] - 1] == '1':
			for i in range(a[1], len(line1)):
				if line1[i] == '1' and line2[i] == '1':
					print('YES')
					done = True
					break
		if done == False:
			print('NO')














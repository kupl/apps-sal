t = int(input())
for _ in range(t):
	n = int(input())
	s = input()

	position_to_step = {(0, 0): 0}
	len_of_min = n+1
	ans = (0, 0)
	pos = (0, 0)

	for i in range(n):
		item = s[i]
		if  item == "U":
			pos = (pos[0], pos[1]+1)
		elif  item == "D":
			pos = (pos[0], pos[1]-1)
		if  item == "R":
			pos = (pos[0]+1, pos[1])
		if  item == "L":
			pos = (pos[0]-1, pos[1])

		if pos in position_to_step:
			if i - position_to_step[pos] < len_of_min:
				len_of_min = i - position_to_step[pos]
				ans = position_to_step[pos], i

		position_to_step[pos] = i+1

	if ans[0] == ans[1]:
		print(-1)
	else:
		print(ans[0]+1, ans[1]+1)


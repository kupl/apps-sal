team_one = input()
team_two = input()
n = int(input())
pts_one = [0 for i in range(100)]
pts_two = [0 for i in range(100)]
for i in range(n):
	line = input()
	t, team, m, card = line.split()
	t = int(t)
	m = int(m)
	fault = 0
	if card == 'y':
		fault = 1
	else: fault = 2
	if team == 'h':
		pts_one[m] += fault
		if pts_one[m] == 2 or (pts_one[m] == 3 and fault == 2):
			print(team_one, m, t)
	elif team == 'a':
		pts_two[m] += fault
		if pts_two[m] == 2 or (pts_two[m] == 3 and fault == 2):
			print(team_two, m, t)


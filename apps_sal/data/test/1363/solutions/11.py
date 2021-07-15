from math import factorial

def bin_search(l, r, x):
	while l < r - 1:
		m = (l+r)//2
		if players[m][0] == x:
			return m
		if players[m][0] < x:
			l = m
		else:
			r = m
	return l

def cmds_in_range(rang):
	roles = []
	temp_rang = [i[1] for i in rang]
	for i in range(3):
		roles.append(temp_rang.count(i))
	if roles[0] < 1 or roles[1] < 2 or roles[2] < 3:
		return 0
	comb_d = factorial(roles[1])//(factorial(roles[1]-2)*2)
	comb_f = factorial(roles[2])//(factorial(roles[2]-3)*6)
	return roles[0] * comb_d * comb_f

input()
players = []
for i in range(3):
	for j in (int(k) for k in input().split()):
		players.append((j, i))
players.sort()
players.append((200001, 0))

count = 0
r = 0
for l in range(len(players) - 5):
	if l == 0:
		inter_cmds = 0
	else:
		inter_cmds = cmds_in_range(players[l:r + 1])
	r = bin_search(l, len(players) - 1, players[l][0] * 2)
	cur_cmds = cmds_in_range(players[l:r + 1])
	count += cur_cmds - inter_cmds
	
print(count)

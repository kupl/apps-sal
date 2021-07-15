p_line = [int(x) for x in input().strip().split(' ')]
size = p_line[0]
		
a = [int(x) for x in input().strip().split(' ')]
num_to_occ = {}
for x in a:
	if x not in num_to_occ:
		num_to_occ[x] = 0
	num_to_occ[x] += 1

topics = []
for _, occ in num_to_occ.items():
	topics.append(occ)
topics.sort(reverse = True)

ba = 0
for start in range(1, topics[0] + 1):	
	my_a = start
	
	act = start
	for i in range(1, len(topics)):
		if act % 2 == 1:
			break
		
		act = act / 2
		if act > 0 and topics[i] >= act:
			my_a += act
		else:
			break
	ba = max(ba, my_a)

print(int(ba))

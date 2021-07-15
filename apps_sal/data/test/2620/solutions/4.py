# No need to use segment Tree because apart from the last 14 numbers, nothing will change since 14! > 2*pow(10, 10)

def modify(rest):
	for i in range(len(rest)):
		prefix[-len(rest)+i] = prefix[-len(rest)+(i-1)] + rest[i]
	# print("prefix", prefix)


def next_perm_direct(permc):	# Gets the next permc lexographically bigger permutation
	rest = [x for x in range(max(1, n-14), n+1)]

	temp = 1
	for i in range(1, len(rest)):
		temp = temp*i

	for i in range(len(rest)-1):
		if permc >= temp:
			change = permc//temp
			rest[i], rest[i+change] = rest[i+change], rest[i]
			rest = rest[:i+1] + list(sorted(rest[i+1:]))
			permc = permc%temp
		temp = temp//(len(rest)-1-i)
	# print("rest", rest)
	modify(rest)


n, q = list(map(int, input().split()))
prefix = [0 for i in range(n+1)]
for i in range(1, n+1):
	prefix[i] = prefix[i-1]+i
# print(prefix)

permc = 0
for _ in range(q):
	quer = list(map(int, input().split()))
	if len(quer) == 2:
		permc += quer[1]
		next_perm_direct(permc)
	else:
		l, r = quer[1], quer[2]
		print(prefix[r]-prefix[l-1])

	



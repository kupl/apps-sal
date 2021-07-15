from sys import stdin
# stdin=open('input.txt')

def input():
	return stdin.readline().strip()


# from sys import stdout
# stdout=open('input.txt',mode='w+')

# def print1(x, end='\n'):
# 	stdout.write(str(x) +end)


# a, b = map(int, input().split())

# l = list(map(int, input().split()))


# # CODE BEGINS HERE.................
from itertools import permutations, combinations


m, n = list(map(int, input().split()))

pairs = []
for i in range(n):
	a, b = list(map(int, input().split()))
	pairs.append((a, b))

if n == 1:
	print('YES')
else:
	possible = set([pairs[0][0], pairs[0][1]])
	flag = True
	for i in range(n):
		if pairs[i][0] in possible or pairs[i][1] in possible:
			continue
		else:
			if len(possible) == 4:
				flag = False
				break
			else:
				possible.add(pairs[i][0])
				possible.add(pairs[i][1])
	if flag:
		possible = list(possible)
		x_y = list(combinations(possible, 2))
		for x, y in x_y:
			x_y_ = set([x, y])
			flag = True
			for i in range(n):
				if pairs[i][0] in x_y_ or pairs[i][1] in x_y_:
					continue
				else:
					flag = False
					break	
			if flag:
				break

	if flag:
		print('YES')
	else:
		print('NO')

# # CODE ENDS HERE....................
# stdout.close()



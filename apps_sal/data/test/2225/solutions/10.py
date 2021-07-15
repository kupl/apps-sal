
from math import floor, log
from sys import stdin, stdout
def update(idx, value, n):
	# print(idx, n)
	nonlocal newL
	idx = idx + 2**n-1
	# print(idx, n)
	newL[idx] = value
	m = len(newL)
	while idx > 1:
		idx //=2
		if(distance(idx, m)  % 2 != 0):
			newL[idx] =  newL[2* idx] | newL[2*idx+1]
		else:
			newL[idx] = newL[2 * idx] ^ newL[2 * idx + 1]

	

def distance(idx, n):
	d = 0
	while True:
		if 2 * idx < n:
			d += 1
			idx = 2 * idx
		else:
			break
	return d



def makeTree(a, n1):
	newL = [0 for _ in a] + a
	n = len(a)
	m = len(newL)

	for idx in reversed(list(range(1,n))):

		if(distance(idx, m)  % 2 != 0):
			newL[idx] =  newL[2* idx] | newL[2*idx+1]
		else:
			newL[idx] = newL[2 * idx] ^ newL[2 * idx + 1]

	return newL



n, m  = list(map(int, input().split()))
a = [int(x) for x in input().split()]
newL = makeTree(a, n)
# print(newL)

for _ in range(0,m):
	idx, value = list(map(int, stdin.readline().split()))
	update(idx , value, n)
	stdout.write(str(newL[1]) + '\n')
	# print(newL)


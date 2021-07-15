'''input
3
0 2 0
1 0 3
'''
from sys import stdin
from copy import deepcopy
from collections import deque



def find_start(pile):
	start = 1
	index = -1

	for i in range(len(pile)):
		if pile[i] == start:
			index = i
			break
	latest = start
	if index != -1:
		flag = True
		for i in range(index, len(pile)):
			if pile[i] == latest:
				latest += 1
			else:
				flag = False
				break

		if flag:
			start = latest
	return start


# 
def check_start(num, op):
	op[0] = 0
	nonlocal arr
	nonlocal barr

	mydict = [0] * (n + 1)
	for i in range(len(arr)):
		mydict[arr[i]] += 1
		
	# print(mydict)
	zeroes = mydict[0]

	pile = deque(barr[:])


	# inserting the zeroes initially
	for i in range(num):
		if zeroes > 0:
			op[0] += 1
			pile.append(0)
			zeroes -= 1
			mydict[0] -= 1
		else:
			return False

		element = pile.popleft()


		# updating the dictionary
		mydict[element] += 1
	
		# checking if it is zero
		if element == 0:
			zeroes += 1
	# print(mydict)

	# inserting the numbers
	start = find_start(barr)
	# print(start)
	for i in range(start, n + 1):
		# print(pile)
		if mydict[i] > 0:
			op[0] += 1
			pile.append(i)
			mydict[i] -= 1
			element = pile.popleft()
			mydict[element] += 1
		else:
			return False
	return True


# main starts
n = int(stdin.readline().strip())
arr = list(map(int, stdin.readline().split()))
barr = list(map(int, stdin.readline().split()))
start = 0
end = 2 * n
op = [0]

if check_start(0, op):
	print(op[0])
	return

pos = [0] * (n + 1)
for i in range(n):
	pos[barr[i]] = i + 1

ans = -float('inf')
for i in range(1, n + 1):	
	ans = max(pos[i] - i  + 1 + n, ans)
print(ans)

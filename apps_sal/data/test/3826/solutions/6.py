'''input
4
1 1 2 2
'''
from sys import stdin
from copy import deepcopy


def get_dict(arr, n):
	mydict = dict()
	for i in range(n):
		if arr[i] in mydict:
			mydict[arr[i]] += 1
		else:
			mydict[arr[i]] = 1

	more = 0
	for i in mydict:
		if mydict[i] > 1:
			more += 1
	return more, mydict


# main starts
n = int(stdin.readline().strip())
arr = list(map(int, stdin.readline().split()))
ans = float('inf')
more, mydict = get_dict(arr, n)
if more == 0:
	ans = 0
	print(ans)
	return

for i in range(n):
	t = more
	tdict = deepcopy(mydict)
	for j in range(i, n):
		tdict[arr[j]] -= 1
		if tdict[arr[j]] == 1:
			t -= 1
		if t == 0:
			ans = min(ans,  abs(i - j) + 1)


print(ans)

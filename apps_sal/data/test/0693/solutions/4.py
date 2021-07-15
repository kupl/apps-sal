import random, math
from copy import deepcopy as dc
from bisect import bisect_left, bisect_right



# Function to call the actual solution
def solution(li, li1):
	freq = {}
	for i in range(len(li1)):
		if li1[i]:
			freq[i+1] = li1[i]
	
	maxi = len(li)
	# Exclusive ranges j - i 
	i = 0
	j = 0
	req = dc(freq)
	cur_freq = [0]*(len(li1) + 1)
	flag = False
	while i < len(li):
		while len(req) and j < len(li):
			cur_freq[li[j]] += 1
			if li[j] in req:
				req[li[j]] -= 1
				if req[li[j]] <= 0:
					del req[li[j]]
			j += 1
		if len(req):
			break
		flag = True
		maxi = min(maxi, j - i)
		cur_freq[li[i]] -= 1
		if li[i] in freq and cur_freq[li[i]] < freq[li[i]]:
			req[li[i]] = req.get(li[i], 0) + 1
		i += 1
	if not flag:
		return -1
	return maxi - sum(li1)



# Function to take input
def input_test():
	# for _ in range(int(input())):
		# n = int(input())
		a, b = list(map(int, input().strip().split(" ")))
		# a, b, c = map(int, input().strip().split(" "))
		li = list(map(int, input().strip().split(" ")))
		li1 = list(map(int, input().strip().split(" ")))
		out = solution(li, li1)
		print(out)

# Function to check test my code
def test():
	pass


input_test()
# test()


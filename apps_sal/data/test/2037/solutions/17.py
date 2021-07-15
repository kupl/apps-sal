import sys
import math

def read_int():
	return int(input().strip())

def read_int_list():
	return list(map(int,input().strip().split()))

def read_string():
	return input().strip()

def read_string_list(delim=" "):
	return input().strip().split(delim)

###### Author : Samir Vyas #######
###### Write Code Below    #######

n,m = read_int_list()
arr = read_int_list()

diki = {}

for i in range(m):
	diki[arr[i]] = diki.get(arr[i],0) + 1

	if len(diki) == n:
		to_be_deleted = []
		for k in diki:
			diki[k] -= 1
			if diki[k] <= 0:
				to_be_deleted.append(k)

		for t in to_be_deleted:
			diki.pop(t)

		print(1,end="")

	else:
		print(0,end="")

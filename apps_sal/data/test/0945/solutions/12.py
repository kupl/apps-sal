# read the inputs
#maintain a table of values that you have seen.
# maintain the current and the next entry
# for every next entry , check if any point in the hash table has that value.

import sys
n=int(input())
values=[int(v) for v in input().split()]
# Previous solution
prev=values[0]
explored=[]
for i in range(1,n,1):
	cur=values[i]
	less,great = min(cur,prev),max(cur,prev)
	for val in explored:
		start,end = val
		if (less < start and great > start and less < end and great < end) or (less < end and great > end and less > start and great > start): 
			print('yes')
			return
	explored.append((less,great))
	prev=cur	
print('no')

'''explored = []
prev=values[0]
for v in values:
	if v < prev:
		for e in explored:
			if v < e and e < prev:
				print('yes')
				return
	elif v > prev:
		for e in explored:
			if v > e and e > prev:
				print('yes')
				return
	prev=v
	explored.append(v)
print('no')'''


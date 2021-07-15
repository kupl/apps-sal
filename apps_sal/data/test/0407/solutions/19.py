import math
import operator
num = int(input())
total = 0
store = {}
nonzero = []
_max = 0
for i in range(num):
    _in = input()
    if _max < len(_in):
    	_max = len(_in)
    if _in[0] not in nonzero:
    	nonzero.append(_in[0])
    for j in range(len(_in)-1,-1,-1):
    	if _in[j] in store:
    		store[_in[j]] += pow(10,len(_in)-j-1)
    	else:
    		store[_in[j]] = pow(10,len(_in)-j-1)
x = store
sorted_x = sorted(x.items(), key=operator.itemgetter(1))

used = False
cur = 1
for i in range(len(sorted_x)-1,-1,-1):
	if sorted_x[i][0] not in nonzero and used == False:
		used = True
	else:
		total += sorted_x[i][1] * cur
		cur += 1
print(total)

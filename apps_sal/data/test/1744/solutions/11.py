import math
import heapq
import copy
from collections import OrderedDict
from collections import deque  



t=list(map(int,input().split()))
d=t[1]
k=list(map(int,input().split()))
m=[0]*101
ans=list()

time=0
for i in range(t[0]):
	time=time+k[i]
	if((d-time)>=0):
		ans.append(0)
		m[k[i]]=m[k[i]]+1
		
	else:
		count=0
		test=time
		for j in range(100,-1,-1):
			if(test<=d):
				break
			if(m[j]>0):
				cur=m[j]
				vv=cur*j
				if(abs(test-vv)<=d):
					if(vv<test or vv>test):
						x=math.ceil((test-d)/j)
						if(x<=cur):
							count=count+x
							test=test-(x*j)
						else:
							count=count+cur
							test=test-(cur*j)
					else:
						count=count
						test=test-vv

				else:
					count=count+m[j]
					test=test-vv
		ans.append(count)
		m[k[i]]=m[k[i]]+1
print(*ans)

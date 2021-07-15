#from math import ceil, log

t = 1#int(input())
for test in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    l = -1
    h = n
    curMax = 0
    sum1 = 0
    sum3 = 0
    while l<h:
    	if sum1==sum3:
    		curMax = max(curMax, sum1)
    		l+=1
    		sum1+=arr[l]
    	elif sum1<sum3:
    		l+=1
    		sum1+=arr[l]
    	else:
    		h-=1
    		sum3+=arr[h]
    print(curMax)




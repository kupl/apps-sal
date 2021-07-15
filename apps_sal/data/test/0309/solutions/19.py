import math
l,r = list(map(int,input().strip().split()))
lr = int(math.log(r)/math.log(2))
ll = int(math.log(l)/math.log(2))

if lr > ll:
	lr+=1
	ans = 1<<lr
	ans-=1
	print(ans)
else:
	ans = 0
	fl = False
	for i in range(lr,-1,-1):
		if l&(1<<i) == r&(1<<i) and fl == False:
			continue 
		elif l&(1<<i) != r&(1<<i):
			ans = ans + (1<<i)
			fl = True
		elif fl == True:
			ans = ans + (1<<i)
				
	print(ans)
##101100101110010110010011110101101110101101111010110010011000
##100101001000010011010111110011010001111010111010011001111010


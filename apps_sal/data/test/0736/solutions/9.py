import math

#input

n,m=list(map(int,input().split()))



#variables
minimum=math.ceil(n/2)
i=minimum-1



#main

while True:
	i+=1
	if i%m==0:
		print(i)
		quit()
	if i==n:
		print(-1)
		quit()


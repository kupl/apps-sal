for i in range(int(input())):
	n=int(input())
	tmp=3
	while(True):
		if(n%tmp==0):
			print(int(n/tmp))
			break
		else:
			tmp=tmp*2+1

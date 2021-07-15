t=int(input())
for nt in range(t):
	n=int(input())
	ln=list(map(int,input().split()))
	m=int(input())
	lm=list(map(int,input().split()))
	lne,lno,lme,lmo=0,0,0,0
	for i in ln:
		if i%2==0:
			lne+=1
		else:
			lno+=1
	for i in lm:
		if i%2==0:
			lme+=1
		else:
			lmo+=1
	print (lne*lme+lno*lmo)	

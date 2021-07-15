import sys
#from math import *
def eprint(*args):
    print(*args, file=sys.stderr)
zz=1
if zz:
	input=sys.stdin.readline
else:	
	sys.stdin=open('input.txt', 'r')
	sys.stdout=open('output2.txt','w')
t=int(input())
while t>0:
	t-=1	
	n,k=map(int,input().split())
	s=list(input().rstrip())
	s.sort()
	d={}
	a=["" for i in range(k)]
	for i in range(k):
		a[i%k]+=s[i]
	

	j=0	
	i=k

	if len(set(s[k:]))==1:
		for i in range(k,len(s)):
			a[j%k]+=s[i]
			j+=1
			if j==k or a[j][0]>a[0][0]:
				j=0
	else:
		for i in range(k,len(s)):
			a[j%k]+=s[i]		
	#print(a)
	print(max(a))	

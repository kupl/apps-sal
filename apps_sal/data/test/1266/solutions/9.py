n=int(input())
temp=input().split()
x0=int(temp[0])
y0=int(temp[1])

N=['T',10**20]
NE=['T',10**20]
E=['T',10**20]
SE=['T',10**20]
S=['T',10**20]
SW=['T',10**20]
W=['T',10**20]
NW=['T',10**20]

for i in range(n):
	temp=input().split()
	x=int(temp[1])
	y=int(temp[2])
	if x-x0==0 and y-y0>0 and y-y0<N[1]:
		N=[temp[0],y-y0]
	elif x-x0==y-y0 and x-x0>0 and x-x0<NE[1]:
		NE=[temp[0],x-x0]
	elif y-y0==0 and x-x0>0 and x-x0<E[1]:
		E=[temp[0],x-x0]
	elif x-x0==-(y-y0) and x-x0>0 and x-x0<SE[1]:
		SE=[temp[0],x-x0]
	elif x-x0==0 and y-y0<0 and y0-y<S[1]:
		S=[temp[0],y0-y]
	elif x-x0==y-y0 and x-x0<0 and x0-x<SW[1]:
		SW=[temp[0],x0-x]
	elif y-y0==0 and x-x0<0 and x0-x<W[1]:
		W=[temp[0],x0-x]
	elif x-x0==-(y-y0) and x-x0<0 and x0-x<NW[1]:
		NW=[temp[0],x0-x]

if 'R' in [N[0],E[0],S[0],W[0]] or 'B' in [NE[0],SE[0],SW[0],NW[0]]:
	print("YES")
elif 'Q' in [N[0],E[0],S[0],W[0],NE[0],SE[0],SW[0],NW[0]]:
	print("YES")
else:
	print("NO")

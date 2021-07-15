F=str.count
I=input
R=lambda:map(int,I().split())
p=I()
B=F(p,'B')
S=F(p,'S')
C=F(p,'C')
b,s,c=R()
q,w,e=R()
p=int(I())
l=-1
r=10**20
while l<r-1:
	m=(l+r)//2
	if q*max(0,B*m-b)+w*max(0,S*m-s)+e*max(0,C*m-c)<=p:l=m
	else:r=m
print(l)

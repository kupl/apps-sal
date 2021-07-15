def minimum(floor,j,s,n,m):
	if(s==[]):
		return 0
	if(floor==0):
		if(j==0):
			return s[floor].rfind('1')
		else:
			return m+1-s[floor].find('1')
	if(j==0):
		return min(2*s[floor].rfind('1')+1+minimum(floor-1,0,s,n,m),m+2+minimum(floor-1,m+1,s,n,m))
	else:
		return min(2*(m+1-s[floor].find('1'))+1+minimum(floor-1,m+1,s,n,m),m+2+minimum(floor-1,0,s,n,m))

inp=input().split()
n=int(inp[0])
m=int(inp[1])
s=[]
for i in range(n):
	s.append(input())
counter=0
while(s!=[]):
	if(s[0].find('1')==-1):
		counter+=1
		s.pop(0)
	else:
		break
counter2=0
s2=[]
for val in s:
	if(val.find('1')==-1):
		counter2+=1
	else:
		s2.append(val)

print(minimum(n-1-counter-counter2,0,s2,n,m)+counter2)

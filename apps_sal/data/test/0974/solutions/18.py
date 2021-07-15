n=int(input())
st=[]
ans=0
c=0
for _ in range(2*n):
	s=input()
	if s=="remove":
		if len(st)==0 or c+1==st[-1] :
			if len(st)!=0:
				st.pop(-1)
			c+=1
		else:
			ans+=1
			c+=1
			st=[]	
	else:
		st.append(int(s[4:]))
	#print (st,end=" ")
	#print (ans)	
print (ans)	


temp=[0]
temp2=[1]
ju=int(pow(2,32)-1)
n=int(input())
ans=0
for i in range(n):
	t=input()
	if t=='add':
		ans+=temp2[-1]
		if temp2[-1]==-1:
			print('OVERFLOW!!!')
			return
	elif t=='end':
		temp.pop()
		temp2.pop()
	else:
		tt=t.split()
		temp.append(int(tt[-1]))
		if temp2[-1]<0:
			temp2.append(-1)
		else:
			ttt=temp2[-1]*int(tt[-1])
			if ttt>ju:
				temp2.append(-1)
			else:
				temp2.append(temp2[-1]*int(tt[-1]))
		
if ans>ju:
	print('OVERFLOW!!!')
else:
	print(ans)

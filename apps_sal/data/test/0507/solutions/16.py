n = int(input())
l1 = list(map(int,input().split()))
l2 = list(map(int,input().split()))

tot = 0

done = [False for i in range(n+1)]

for i in range(n):
	if(l1[i]!=l2[i]):
		tot+=1
	else:
		done[l1[i]] = True

ans = []
if(tot==1):
	for i in range(n):
		if(l1[i]==l2[i]):
			ans.append(l2[i])
		else:
			for j in range(1,n+1):
				if(done[j]==False and l1[i]!=j and l2[i]!=j):
					ans.append(j)
					break
elif(tot==2):
	l = []
	for i in range(n):
		if(l1[i]==l2[i]):
			ans.append(l2[i])
		else:
			ans.append(0)
			l.append(i)

	ok = True
	_ans = ans
	for i in range(1,n+1):
		if(done[i]==False):
			if(ok==True):
				_ans[l[0]] = i
				ok = False
			else:
				_ans[l[1]] = i
	diff1 = 0
	diff2 = 0
	for i in range(n):
		if(_ans[i]!=l1[i]):
			diff1+=1
		if(_ans[i]!=l2[i]):
			diff2+=1
	if(diff1==1 and diff2==1):
		ans = _ans
	else:
		ok = True
		_ans = ans
		for i in range(1,n+1):
			if(done[i]==False):
				if(ok==True):
					_ans[l[1]] = i
					ok = False
				else:
					_ans[l[0]] = i
		ans = _ans
for i in ans:
		print(i,end=" ")


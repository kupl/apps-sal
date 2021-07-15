n, m = list(map(int,input().split()))
p = list(map(int,input().split()))
mindex = p.index(m)
ldict = {}
rdict = {}
diff = 0
ans = 0
ldict[0] = 1
rdict[0] = 1
for i in range(mindex-1,-1,-1):
	if p[i] < m:
		diff-=1
	else:
		diff+=1
	if diff in ldict.keys():
		ldict[diff] += 1
	else:
		ldict[diff] = 1
diff = 0
for i in range(mindex+1,n):
	if p[i] < m:
		diff-=1
	else:
		diff+=1
	if diff in rdict.keys():
		rdict[diff] += 1
	else:
		rdict[diff] = 1
ldictkey = ldict.keys()
for num in ldictkey:
	if -num in rdict.keys():
		ans += ldict[num] * rdict[-num]
	if -num+1 in rdict.keys():
		ans += ldict[num] * rdict[-num+1]
print(ans)

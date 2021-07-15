n = int(input())
temp = input()
st=[c for c in temp]
temp=set(st)
nT=len(temp)
s={}
for i in temp:
	s[i]=0
currT=set()
i=0
j=0
minL=10**10
for i in range(len(st)):
	currT.add(st[i])
	s[st[i]]+=1
	while j<i and (s[st[j]]>1):
		s[st[j]]-=1
		j+=1
	if len(currT)==nT:
		minL=min(minL,i-j+1)

print(minL)

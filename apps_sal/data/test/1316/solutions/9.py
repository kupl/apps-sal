n,k=list(map(int,input().split()))
s=input()
d={}
i,j=0,0
while i<len(s):
	j=i
	while j<len(s) and s[j]==s[i]:
		j+=1
	ans=(j-i)//k
	if s[i] in d:
		d[s[i]]+=ans
	else:
		d[s[i]]=ans
	i=j
print(max(d.values()))


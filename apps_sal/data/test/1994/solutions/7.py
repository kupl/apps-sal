def prefixFunction(s):
	j=0
	p=[0 for x in s]
	for i in range(1,len(s)):
		while j>0 and s[j]!=s[i]:
			j=p[j-1]
		if (s[j]==s[i]):j+=1
		p[i]=j
	return p
s=input()
p=prefixFunction(s)
n=len(s)
freq=[0 for i in range(n)]

for i in range(n):
    freq[p[i]]+=1

for i in range(n-1,0,-1):
    freq[p[i-1]]+=freq[i]

pos =n-1
ans=[[n,1]]
while pos>0:
        if p[pos]>1:
                ans.append([p[pos],freq[p[pos]]+1])
        pos=p[pos]-1

if len(s)>1 : 
        f= s.count(s[0])
        if s[0] == s[len(s)-1] : ans.append([1,f])
print(len(ans))
for i in sorted (ans):
    print(i[0],i[1])

    


import itertools
 
N,M=map(int,input().split())
s=[list(map(int,input().split())) for _ in range(M)]
 
lst=[x for x in range(1,N+1)]   
l=itertools.permutations(lst)
 
ans=0
cnt=0
for num in l:
	if num[0]==1:
		for j in range(N-1):
			if [num[j], num[j+1]] in s or [num[j+1], num[j]] in s:
				cnt+=1
	if cnt==N-1:
		ans+=1
		cnt=0
	else:
		cnt=0
 
print(ans)

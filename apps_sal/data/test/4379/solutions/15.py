n=int(input())
a=list(map(int ,input().split() ) )
d={}
maxn=0
max_ind=0

for ai in a:
	d[ai]=d.get(ai-1,0)+1

for key in d.keys():
	if(d[key] >maxn):
	  maxn=d[key]
	  max_ind=key

start= max_ind-maxn+1
print(maxn)
i=0
for ai in a:
	i+=1
	if(ai==start):
                 print(i,end=' ')
                 start+=1
                 
	

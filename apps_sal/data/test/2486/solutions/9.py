from collections import Counter
N,K=list(map(int, input().split()))
a=list(map(int, input().split()))
a.sort()
a.reverse()

tmp=[]
tmp_sum=0
b=[]
for i in a:
	if tmp_sum+i>=K:
		b.append(i)	
	else:
		tmp.append(i)
		tmp_sum+=i

if len(b)==0:
	print(N)
else:
	min_num=b[-1]
	c=Counter(a)
	print(N-(a.index(min_num)+c[min_num]))


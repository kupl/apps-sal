import itertools
N,M = map(int,input().split())
ball = list(range(2,2*N+1,2))+list(range(1,2*M,2))
count=0
for i,j in list(itertools.combinations(ball,2)):
  	if (i+j)%2==0:count+=1
print(count)

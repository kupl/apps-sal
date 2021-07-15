N,Q=list(map(int, input().split()))
S=input()
Ssum=[0]*N

now=S[0]
cnt=0
for i in range(1,N):
	next=S[i]
	if now=="A" and next=="C":
		cnt+=1
	Ssum[i]=cnt
	now=next

for q in range(Q):
	l,r=list(map(int, input().split()))
	print((Ssum[r-1]-Ssum[l-1]))



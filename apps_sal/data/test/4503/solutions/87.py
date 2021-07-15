H,N=list(map(int,input().split()))
A=list(map(int,input().split()))
s=0
flg=True
for i in range(N):
  s+=A[i]
  if s>=H:
    print('Yes')
    flg=False
    break
if flg:
	print('No')


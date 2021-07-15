N=int(input())
A=[0,0]
A[0]=list(map(int,input().split()))
A[1]=list(map(int,input().split()))
count=[0]*N
for i in range(N) :
  count[i]+=sum(A[0][:i+1])+sum(A[1][i:])
print(max(count))

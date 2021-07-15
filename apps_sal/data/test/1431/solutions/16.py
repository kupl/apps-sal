N=int(input())
A=list(map(int,input().split()))
ans=[0]*N
for i in range(N):
  n=N-i
  add=A[n-1]
  n_tmp=n
  while True:
    n_tmp+=n
    if n_tmp>N:break
    if ans[n_tmp-1]:
      add=0 if add else 1
  if add:
    ans[n-1]=1
print(ans.count(1))
ans2=[]
for i,v in enumerate(ans):
  if v:
    ans2.append(i+1)
print(*ans2)

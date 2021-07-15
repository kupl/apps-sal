N,K=map(int,input().split())
S=input()
a=[0]
for i in range(1,N):
  if S[i-1]!=S[i]:
    a.append(i)
a.append(N)
l=len(a)
ans=[]
for i in range(l-1):
  if S[a[i]]=='0':
    ans.append(a[min(i+2*K,l-1)]-a[i])
  else:
    ans.append(a[min(i+2*K+1,l-1)]-a[i])
print(max(ans))

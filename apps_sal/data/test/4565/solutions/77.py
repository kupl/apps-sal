N=int(input())
S=input()
ans=S.count("W")
ans1=-10
for i in range(N):
  if S[i]=="W":
    ans-=1
  if i!=0:
    if S[i-1]=="E":
      ans+=1
  ans1=max(ans,ans1)
print(N-1-ans1)

n=int(input())
s1=input()
s2=input()
mod=10**9+7
if s1[0]==s2[0]:
  cnt=3
  flag=0
  i=1
else:
  cnt=6
  flag=1
  i=2
while i<n:
  if s1[i]==s2[i] and flag==0:
    i+=1
    cnt*=2
  elif s1[i]==s2[i] and flag==1:
    i+=1
    flag=0
  elif s1[i]!=s2[i] and flag==0:
    i+=2
    cnt*=2
    flag=1
  else:
    i+=2
    cnt*=3
  cnt%=mod
print(cnt%mod)

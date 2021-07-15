N=int(input())
S1=input()
S2=input()
mod=1000000007
i=0
array=[]
while i<N:
  if S1[i]==S2[i]:
    array.append(0)
    i+=1
  else:
    array.append(1)
    i+=2
for i in range(len(array)):
  if i==0:
    if array[i]==0:
      ans=3
    else:
      ans=6
  else:
    if array[i]==0:
      if array[i-1]==0:
        ans=ans*2
    else:
      if array[i-1]==0:
        ans=ans*2
      else:
        ans=ans*3
  ans=ans%mod
print(ans)

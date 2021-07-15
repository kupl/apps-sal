S=input()
s=int(S)
mod=2019
c=[0]*(len(S)+1)
d=[0]*2019


c[0]=0
d[0]=1
for i in range(len(S)):
  c[i+1]=(c[i]+int(S[-i-1])*pow(10,i,mod))%mod
  d[c[i+1]]+=1
  
m=0
for i in range(2019):
  m+=d[i]*(d[i]-1)//2

print(m)

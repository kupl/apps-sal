s=input()[::-1]
n=len(s)
cnts=[0]*2019
cnts[0]=1
num=0
for i in range(n):
  num+=int(s[i])*pow(10,i,2019)
  num%=2019
  cnts[num]+=1

ans=0
for cnt in cnts:
  ans+=cnt*(cnt-1)//2
  
print(ans)


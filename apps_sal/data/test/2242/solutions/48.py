s=input()
n=len(s)
rui=[0]
juu=[1]
for i in range(n+5):
  juu.append(juu[-1]*10%2019)  
for i in range(n):
  rui.append((rui[-1]+int(s[n-1-i])*juu[i])%2019)
ama=[0]*2019
for i in range(len(rui)):
  ama[rui[i]]+=1
ans=0
def ui(n):
  return max(0,n*(n-1)//2)
for i in range(2019):
  ans+=ui(ama[i])
print(ans)  

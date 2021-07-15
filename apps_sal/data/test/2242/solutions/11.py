from collections import Counter

S=input()

rlist=[0]
for i in range(len(S)):
  rlist.append((rlist[-1]+int(S[-i-1])*pow(10,i,2019))%2019)
  
c = Counter(rlist)
c[0] -= 1

def nC2(n):
  return n*(n-1)//2
  
ans = c[0]
for k in c.keys():
  if c[k] >= 2:
    ans += nC2(c[k])
    
print(ans)

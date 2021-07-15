import collections
def gcd(a,b):
  if b==0:
    return a
  else:
    return gcd(b,a%b)
K=int(input())
cnt=collections.defaultdict(int)
for a in range(1,K+1):
  for b in range(1,K+1):
    cnt[gcd(a,b)]+=1
ans=0
for c in range(1,K+1):
  for gcd_of_ab in cnt.keys():
  	ans+=gcd(gcd_of_ab,c)*cnt[gcd_of_ab]
print(ans)

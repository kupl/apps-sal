from collections import Counter

n=int(input())
l=[int(input()) for i in range(n)]

l=Counter(l)

cnt=0

for i in list(l.values()):
  if i%2==0:
    cnt+=1
    
print((len(l)-cnt))


from collections import Counter
n=int(input())
a=list(map(int,input().split()))
amod4=list([x%4 for x in a])
d=Counter(amod4)
if n-d[0]-d[2]<d[0]+1:
  print('Yes')
elif d[2]==0 and n==2*d[0]+1:
  print('Yes')
else:
  print('No')


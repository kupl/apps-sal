n=int(input())
l=list(map(int, input().split()))
l1=l[0::2]
l2=l[1::2]
import collections
c1 = collections.Counter(l1)
#print(c1)
# Counter({'a': 4, 'c': 2, 'b': 1})
c2 =collections.Counter(l2)  
c0 =collections.Counter(l)
if len(c0)==1:
  print((int(n/2)))
else:
  if c1.most_common()[0]==c2.most_common()[0]:
    print((min(n-c1.most_common()[0][1]-c2.most_common()[1][1], n-c1.most_common()[1][1]-c2.most_common()[0][1])))
  else:
    print((n-c1.most_common()[0][1]-c2.most_common()[0][1]))
    


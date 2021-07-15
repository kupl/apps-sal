import sys
from collections import Counter
n=int(sys.stdin.readline())
i=list(map(float,sys.stdin.readline().split()))
pt=list(map(float,sys.stdin.readline().split()))
o=list(map(float,sys.stdin.readline().split()))
a=Counter(i)

b=Counter(pt)
q=Counter(o)

gg=a-b
for i in gg:
  print(int(i))
gg=b-q
for i in gg:
  print(int(i))

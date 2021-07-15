n = int(input())
a = list(map(int,input().split()))
from collections import Counter
l = Counter(a)
for i in range(n):
  print(l[i+1])

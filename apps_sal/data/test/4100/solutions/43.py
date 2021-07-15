n,k,q = map(int,input().split())
win = [int(input()) for i in range(q)]
from collections import Counter
winC = Counter(win)
l = [k-q]*n
for key,value in winC.items():
  l[key-1] += value
for j in range(n):
  if l[j]<=0:
    print("No")
  else:
    print("Yes")

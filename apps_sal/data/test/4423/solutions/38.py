n = int(input())
sp = [list(map(str,input().split())) for i in range(n)]
for i in range(1,n+1):
  sp[i-1][1] = int(sp[i-1][1])
  sp[i-1].append(i)
from operator import itemgetter
sp.sort(key = itemgetter(1),reverse = True)
sp.sort(key = itemgetter(0))
for i in range(n):
  print(sp[i][2])

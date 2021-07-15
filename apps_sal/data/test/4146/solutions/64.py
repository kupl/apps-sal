from collections import defaultdict
ODD = defaultdict(int)
EVEN = defaultdict(int)
ALL = set([])
N = int(input())

A = list(map(int,input().split()))
for i in range(N):
  ALL.add(A[i])
  if i%2 == 0:
    EVEN[A[i]] += 1
  else:
    ODD[A[i]] += 1
if len(ALL) == 1:
  ans = N//2
  print(ans)
  return
modd = max(ODD.values())
meven = max(EVEN.values())
mlodd = [];mleven = []
dicodd = sorted(list(ODD.items()), key=lambda x:x[1], reverse = True)
diceven = sorted(list(EVEN.items()), key=lambda x:x[1], reverse = True)
ans = N
if len(dicodd) > 1:
  X = [dicodd[0],dicodd[1]]
else:
  X = [dicodd[0]]
if len(diceven) > 1:
  Y = [diceven[0],diceven[1]]
else:
  Y = [diceven[0]]
#print(X)
#print(Y)
for x,v in X:
  for y,w in Y:
    if x == y:
      continue
    temp = N-(v+w)
    ans = min(ans,temp)

print(ans)




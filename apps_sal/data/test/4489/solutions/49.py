import collections

N = int(input())
S = [input() for i in range(N)]
cS = collections.Counter(S)
lS = list(cS.items())
M = int(input())
T = [input() for i in range(M)]
cT = collections.Counter(T)
list1 = []
ans = 0

for i in range(len(lS)):
    
    if lS[i][0] in cT:
        x = lS[i][1] - cT[lS[i][0]]
        
    else:
        x = lS[i][1]
        
    if x > 0:
        list1.append(x)
    
if list1 == []:
  print(0)
else:
  print(max(list1))

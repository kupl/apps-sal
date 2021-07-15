import numpy as np
N, C = map(int, input().split())
s = np.empty(N)
t = np.empty(N)
c = np.empty(N)
for i in range(N):
  s[i], t[i], c[i] =  map(int, input().split())
TimeTable = np.zeros((C,100001))
maxTime = 0
for i in range(N):
  channle = int(c[i] - 1)
  for j in range(int(s[i]),int(t[i])+1):
    TimeTable[channle,j] = 1
  if maxTime < t[i]:
    maxTime = t[i]
MaxRecode = 0
for i in range(int(maxTime)):
  Recode = np.sum(TimeTable[:,i])
  if Recode > MaxRecode:
    MaxRecode = Recode
print(int(MaxRecode))

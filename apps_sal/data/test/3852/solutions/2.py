N = int(input())
Z = list(map(int,input().split()))
A = []
for i in range(N):
  A.append([Z[i],i])
MIN = min(A)
MAX = max(A)
#print(A,MAX,MIN)
#print(MIN,MAX)
ans = []
num = 0
if abs(MIN[0]) > abs(MAX[0]):
  Flag = False
  minloc = MIN[1]
  for i in range(N):
    #print(minloc+1,i+1) #1indexにして出力
    ans.append((minloc+1,i+1))
    num += 1
    A[i][0] += MIN[0]
else:
  Flag = True
  maxloc = MAX[1]
  for i in range(N):
    #print(maxloc+1,i+1)
    ans.append((maxloc+1,i+1))
    num +=1
    A[i][0] += MAX[0]

for i in range(N-1):
  if Flag == True:
    ans.append((i+1,i+2))
  else:
    ans.append((N-i,N-1-i))
  num+=1
print(num)
for i in range(len(ans)):
  print((*ans[i]))



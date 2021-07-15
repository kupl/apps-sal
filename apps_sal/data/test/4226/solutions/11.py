X = list(map(int,input().split()))
legs = 0
flag = 0
for crane in range(X[0]+1):
  turtle = X[0]-crane
  legs = crane*2 + turtle*4
  if(X[1] == legs):
    flag = 1
    break
if(flag == 1):print("Yes")
else:print("No")

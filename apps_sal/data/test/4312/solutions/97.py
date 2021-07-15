N = list(map(int,input().split()))
flag = 0
while(N[0] > 0 and N[2] > 0):
  N[2]=N[2]-N[1]
  if(N[2] <= 0):
    flag = 1
    break
  else:
    N[0] = N[0] - N[3]
    if(N[0] <= 0):
      break
if(flag == 1):print("Yes")
else:print("No")

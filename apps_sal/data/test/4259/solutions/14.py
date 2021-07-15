K = int(input())
N = list(map(int,input().split()))
flag = 0
for i in range(N[0],N[1]+1):
  if( i % K == 0):
    flag = 1
    break
  else:continue
if(flag ==1):print("OK")
else:print("NG")

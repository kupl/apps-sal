h,w,k_=list(map(int,input().split()))
mod=pow(10,9)+7
if w==1:
  print((1))
  return
# 遷移の仕方
sen=[[0]*3 for _ in range(w)]
for j in range(2**(w-1)):
  yoko=[0]*(w-1)
  for k in range(w-1):
    if (j>>k) & 1:
      yoko[k]=1
  flg=True
  for k in range(w-2):
    if yoko[k]==1 and yoko[k+1]==1:
      flg=False
      break
  if not flg:continue
  for k in range(w):
    if k==0:
      if yoko[k]==1:
        sen[k+1][0]+=1
      else:
        sen[k][2]+=1
    elif k<w-1:
      if yoko[k]==1:
        sen[k+1][0]+=1
      elif yoko[k-1]==1:
        sen[k-1][1]+=1
      else:
        sen[k][2]+=1
    else:
      if yoko[k-1]==1:
        sen[k-1][1]+=1
      else:
        sen[k][2]+=1

import numpy as np 
dp=np.zeros((h+1,w),int)
dp[0,0]=1
for i in range(h):
  dp[i+1,0]=sen[0][2]*dp[i,0]+sen[0][1]*dp[i,1]
  for j in range(1,w-1):
    dp[i+1,j]=sen[j][2]*dp[i,j]+sen[j][1]*dp[i,j+1]+sen[j][0]*dp[i,j-1]
  dp[i+1,w-1]=sen[w-1][2]*dp[i,w-1]+sen[w-1][0]*dp[i,w-2]
  dp[i+1]%=mod
print((dp[h,k_-1]))
#print(dp)


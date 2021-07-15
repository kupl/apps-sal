N,K=map(int,input().split())
S=input()

if N==1:
  print(1)
  return

S2=[]
signs=[]
if S[0]=='1':
  sign=1
else:
  sign=0
count = 1
for i in range(1,N):
  if S[i] != S[i-1]:
    S2.append(count)
    signs.append(sign)
    sign = 1- sign
    count = 0
  count += 1
  
S2.append(count)
signs.append(sign)
  
cumS = [0]
for i in range(len(S2)):
  cumS.append(cumS[-1]+S2[i])
  
k = K*2+1
if len(S2)>=k:
  MAX=0
  for i in range(len(S2)-k+1):
    if signs[i] == 1:
      tmp = cumS[i+k]-cumS[i]
      if tmp > MAX:
        MAX = tmp
  
  if signs[0]==0:
    MAX = max(MAX,cumS[k-1]-cumS[0])
  if signs[-1]==0:
    MAX = max(MAX,cumS[-1]-cumS[-k])
    
else:
  MAX=cumS[-1]
  
print(MAX)

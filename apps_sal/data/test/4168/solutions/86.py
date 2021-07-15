N = int(input())
S = list()
if N==0:
  print((0))
  return
elif N>0:
  while N>0:
    S.append(N%2)
    N//=2
  S.append(0)
  S.append(0)
  for i in range(len(S)-1):
    if i%2==1 and S[i]==1:
      S[i+1] += 1
    if S[i]==2:
      S[i]=0
      S[i+1]+=1
else:
  N *= -1
  while N>0:
    S.append(N%2)
    N//=2
  S.append(0)
  S.append(0)
  for i in range(len(S)-1):
    if i%2==0 and S[i]==1:
      S[i+1] += 1
    if S[i]==2:
      S[i]=0
      S[i+1]+=1
  
S.reverse()
while S[0]==0:
  S = S[1:]
ans = ""
for s in S:
  ans += str(s)
print(ans)


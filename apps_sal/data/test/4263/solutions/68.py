S=str(input())
le=len(S)
cnt=0
Ans=0

for i in range(le):
  if S[i] in 'A' or S[i] in 'C' or \
  S[i] in 'G' or S[i] in 'T':
    cnt+=1
    if Ans<cnt:
      Ans=cnt
  else:
    cnt=0

print(Ans)


N=int(input())
S=str(input())
ans=S.count('R')*S.count('G')*S.count('B')

for i in range(N-2):
  for j in range(i+1,N-1):
    if S[i]==S[j]:
      continue
    if 2*j - i < N:
      if S[2*j - i] != S[i] and S[2*j - i] != S[j]:
        ans-=1
print(ans)


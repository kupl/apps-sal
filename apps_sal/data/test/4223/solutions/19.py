n=int(input())
S=input()
ans=1
for i in range(len(S)-1):
  if S[i] != S[i+1]:
    ans += 1
print(ans)

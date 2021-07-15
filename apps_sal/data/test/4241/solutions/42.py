S = input()
T = input()
 
ans = len(S)
for i in range(len(S)-len(T)+1):
  cnt = 0
  for j in range(len(T)):
    if(S[i+j] != T[j]):
      cnt += 1
  ans = min(ans, cnt)
print(ans)

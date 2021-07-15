S=input()
ans = 754
for i in range(len(S)-2):
  ans = min(ans,abs(753-int(S[i:i+3])))
print(ans)

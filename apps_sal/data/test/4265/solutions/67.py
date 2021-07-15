S = input()
T = input()
cnt = 0
for i in range (len(S)):
  if(S[i] == T[i]):continue
  else: cnt = cnt + 1 
print(cnt)

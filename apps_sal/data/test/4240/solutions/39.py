S = input()
T = input()
flag = 0
for i in range(len(S)):
  if S == T:
    flag = 1
    break
  S = S[len(S)-1] + S[0:len(S)-1]
if flag == 1:
  print('Yes')
else:
  print('No')

S = str(input())
T = str(input())
for i in range(len(S)):
  if S[i] != T[i]:
    print('No')
    return
print('Yes')

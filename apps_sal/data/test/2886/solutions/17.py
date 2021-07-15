S=input()
n=len(S)
 
for i in range(n-1):
  if S[i] == S[i+1]:
    print(i+1, i+2)
    return
for i in range(n-2):
  if S[i] == S[i+2]:
    print(i+1, i+3)
    return

print(-1, -1)

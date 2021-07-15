N = int(input())
S = input()
L = [0]*(N+1)
for i in range(N):
  if S[i]=="E":
    L[i+1] = L[i]+1
  else:
    L[i+1] = L[i]
print(min(i-L[i]+L[N]-L[i+1] for i in range(N)))

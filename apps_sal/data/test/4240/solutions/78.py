s = str(input())
t = str(input())
N = len(s)
S = [0] * N
T = [0] * N

for i in range(N):
  S[i] = s[i]
  T[i] = t[i]
  
for i in range(N):
  for j in range(N):
    if j == 0:
      x = S[j]
      S[j] = S[j + 1]
    elif 1 <= j < N - 1:
      S[j] = S[j + 1]
    else:
      S[j] = x
  #print(S)    
  if S == T:
    print("Yes")
    return
    
print("No")    
      
      


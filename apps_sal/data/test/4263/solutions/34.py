S = input()

ans = 0
N = len(S)
for i in range(N):
  for j in range(i+1, N+1):
    T = list(S[i:j])
    M = len(T)

    flag = True
    for k in range(M):
      if T[k] != 'A' and T[k] != 'C' and T[k] != 'G' and T[k] != 'T':
        flag = False
        break
    if flag: ans = max(ans, M)
      
print(ans)

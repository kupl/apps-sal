N = int(input())
S = input()
C = {"R", "G", "B"}
cumsum = {c:[0 for i in range(N)] for c in C}

for i in range(N):
  s = S[i]
  cumsum[s][i] = 1
for i in range(2, N+1):
  for c in C:
    cumsum[c][-i] = cumsum[c][-i] + cumsum[c][-(i-1)]
#print(cumsum)
ans = 0
for i in range(N-2):
  s = S[i]
  a, b = C - {s}
  ans += cumsum[a][i]*cumsum[b][i]

for i in range(1, (N-1)//2 + 1):
  for j in range(N-2*i):
    #print(j, j+i, j+2*i, S[j]+S[j+i]+S[j+2*i])
    if S[j] != S[j+i] and S[j+i] != S[j+2*i] and S[j] != S[j+2*i]:
      ans -= 1
print(ans)


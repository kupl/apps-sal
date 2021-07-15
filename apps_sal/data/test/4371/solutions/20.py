S = str(input())

N = len(S)
X = []
for i in range(N-2):
  tmp = 100*int(S[i]) + 10*int(S[i+1]) + int(S[i+2])
  X.append(abs(753 - tmp))
print(min(X))

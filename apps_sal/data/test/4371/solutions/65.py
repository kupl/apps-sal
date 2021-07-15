S = str(input())

N = len(S)
X = []
for i in range(N-2):
  X.append(abs(753 - int(S[i:i+3])))
print(min(X))

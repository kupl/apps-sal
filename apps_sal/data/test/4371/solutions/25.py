S = input()
a = 999
for i in range(len(S)-2):
  X = int(S[i]+S[i+1]+S[i+2])
  if a > abs(X -753):
    a = abs(X -753)
print(a)

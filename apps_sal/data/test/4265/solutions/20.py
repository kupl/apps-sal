S = input()
T = input()
l = len(S)
C = 0
for i in range(l):
  if not S[i]==T[i]:
    C = C +1
print(C)

S = input()
T = input()
s = 0
for i in range(len(S)):
  if S[i] != T[i]:
    s += 1
print(s)

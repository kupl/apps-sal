s = input()
S = ""
for i in s:
  if i == "B":
    S = S[:-1]
  else:
    S += i
print(S)

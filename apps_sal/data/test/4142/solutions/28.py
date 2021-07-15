S = list(input())
ans = True
for i in range(len(S)):
  if i % 2 != 0:
    if S[i] != "L" and S[i] != "U" and  S[i] != "D":
      ans = False
  else:
    if S[i] != "R" and S[i] != "U" and S[i] != "D":
      ans = False
if ans:
  print("Yes")
else:
  print("No")

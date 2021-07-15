A,B = map(int,input().split())
S = str(input())
for i in range(len(S)):
  if i < A:
    if not S[i].isnumeric():
      print("No")
      return
  elif i == A:
    if S[i] != "-":
      print("No")
      return
  else:
    if not S[i].isnumeric():
      print("No")
      return
print("Yes")

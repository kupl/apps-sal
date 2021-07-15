S = input()
judge = True
for n in range(len(S)):
  if n % 2 == 0:
    if S[n] not in ["R","U","D"]:
      judge = False
      break
  else:
    if S[n] not in ["L","U","D"]:
      judge = False
      break
if judge:
  print("Yes")
else:
  print("No")

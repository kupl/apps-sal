s = input()
stk = []
for ch in s:
  if len(stk) > 0 and stk[-1] == ch:
    stk.pop()
  else:
    stk.append(ch)
if len(stk) == 0:
  print("Yes")
else:
  print("No")


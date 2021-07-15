n = int(input());
s = list(input())
stk = []

for i in range(n):
  if s[i] == ')' and len(stk) > 0 and stk[-1][0] == '(':
    stk.pop()
  else:
    stk.append([s[i], i + 1])

if n % 2 == 1 or len(stk) == 0:
  print(0)
elif len(stk) == 2 and stk[0][0] == stk[1][0]:
  if stk[0][0] == '(':
    print((n - stk[1][1]) // 2 + 1)
  else:
    print(stk[0][1] // 2 + 1)
else:
  print(0)

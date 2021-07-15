t = int(input())
for i in range(t):
  n = int(input())
  s = input()
  ok = False
  for i in range(n):
    if s[i] == '8' and i + 11 <= n:
      ok = True
      break
  if ok:
    print('YES')
  else:
    print('NO')

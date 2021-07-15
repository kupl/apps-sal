s = input()
if 4 < len(s) < 6:
  print('No')
  return

if s[::-1] != s:
  print('No')
  return
s = s[:len(s)//2]
if s[::-1] != s:
  print('No')
  return
print('Yes')

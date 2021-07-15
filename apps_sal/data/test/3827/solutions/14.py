s = input()
i = 0
n = len(s)
while i < n-1:
   if ord(s[i]) <= ord(s[i+1]):
      i += 1
   else:
      break
if i == n-1 and s.count('a') > 0 and s.count('b') > 0 and (s.count('c') == s.count('a') or s.count('c') == s.count('b')):
   print('YES')
else:
   print('NO')


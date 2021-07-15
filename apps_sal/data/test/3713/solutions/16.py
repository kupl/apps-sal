n = int(input())
s = input()
cnt = 1
last = s[0]
for i in range(1, len(s)):
  if s[i] != last:
    cnt += 1
    last = s[i]
    
if s.count('111') or s.count('000') or s.count('00')+s.count('11') > 1:
  print(cnt+2)
elif s.count('11')+s.count('00'):
  print(cnt+1)
else:
  print(cnt)

import sys
inp = sys.stdin
s = inp.readline()
cnt = 0
for i in range(len(s) - 1):
  if s[i] not in s[i + 1:]:    
    cnt += 1    
if cnt % 2 == 0:
  print("CHAT WITH HER!")
else:
  print("IGNORE HIM!")

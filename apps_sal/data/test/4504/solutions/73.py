s = input()
s=s[:-1]
ans = 0
for i in range(1, len(s)):
  if i*2 > len(s):
    break
  
  if s[0:i] == s[i:i*2]:
    ans = i*2
    
print(ans)

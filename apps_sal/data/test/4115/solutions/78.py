s=list(input())
r=list(reversed(s))
c=0

for i in range(len(s)):
  if s[i]!=r[i]:
    c+=1

print(c//2)

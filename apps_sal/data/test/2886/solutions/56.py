s=input()
n=len(s)

if n==2:
  if s[0]==s[1]:
    print(1, 2)
  else:
    print(-1, -1)
  return

for i in range(n-2):
  t=s[i:i+3]
  if t[0]==t[1] or t[1]==t[2] or t[0]==t[2]:
    print(i+1, i+3)
    return
print(-1, -1)

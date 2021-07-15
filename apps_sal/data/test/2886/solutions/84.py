s=input()
n=len(s)
for i in range(n-1):
  t=s[i:i+2]
  if t[0]==t[-1]:
    print((i+1,i+2))
    return
for i in range(n-2):
  t=s[i:i+3]
  if t[0]==t[-1] and t[0]!=t[1]:
    print((i+1,i+3))
    return
print((-1,-1))


def f(s):
  t="abacaba"
  for i in range(7):
    if s[i]!="?" and t[i]!=s[i]:return False
  return True
def g(s):
  c=0
  for i in range(7,len(s)+1):
    if s[i-7:i]=="abacaba":c+=1
  return c

for _ in range(int(input())):
  n=int(input())
  s=input()
  if g(s)>1:
    print("No")
    continue
  if "abacaba" in s:
    print("Yes")
    print(s.replace("?","z"))
    continue
  flag=False
  for i in range(7,len(s)+1):
    if f(s[i-7:i]):
      t=(s[:i-7]+"abacaba"+s[i:]).replace("?","z")
      if g(t)>1:continue
      print("Yes")
      print(t)
      flag=True
      break
  if not(flag):print("No")

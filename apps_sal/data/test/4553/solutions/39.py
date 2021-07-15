a,b=map(int,input().split())
s=str(input())
e=["0",'1','2','3','4','5','6','7','8','9']
for i in range(len(s)):
  if a==i:
    if s[i]!='-':
      print("No")
      return
  else:
    if s[i] not in e:
      print("No")
      return

print("Yes")

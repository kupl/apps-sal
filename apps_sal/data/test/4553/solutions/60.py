import re
a,b = list(map(int,input().split()))
s = input()
if re.search(r"[0-9][0-9]*",s[0:a]):
  if s[a]=="-":
    if re.search(r"[0-9][0-9]*",s[(a+1):]):
      print("Yes")
      return
print("No")

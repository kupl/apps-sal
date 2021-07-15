import re
a,b = list(map(int,input().split()))
s = input()
if s[a]=="-":
  if "-" not in s[:a]+s[(a+1):]:
    print("Yes")
    return
print("No")

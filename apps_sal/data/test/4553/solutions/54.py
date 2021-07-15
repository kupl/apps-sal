a,b=map(int,input().split())
n = input()
if n[0:a].isdecimal() and n[a]=="-" and n[a+1:a+b+1].isdecimal():
  print("Yes")
else:
  print("No")

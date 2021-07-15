a,b=map(int,input().split())
S=input()
for i in range(len(S)):
  if i==a:
    if S[i]!="-":
      print("No")
      break
  else:
    try:
      Si = int(S[i])
    except:
      print("No")
      break
else:
  print("Yes")

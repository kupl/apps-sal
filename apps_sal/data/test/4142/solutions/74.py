S=input()
Count=0
for i in range(len(S)):
  if (i+1)%2==0 and (S[i]=="L" or S[i]=="U" or S[i]=="D"):
    Count+=1
  if (i+1)%2==1 and (S[i]=="R" or S[i]=="U" or S[i]=="D"):
    Count+=1
if Count==len(S):
  print("Yes")
else:
  print("No")

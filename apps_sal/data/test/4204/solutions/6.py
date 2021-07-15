s=str(input())
k=int(input())
con=0
for i in s:
  if i=="1":
    con+=1
  else:
    break
if con>=k:
  print(1)
else:
  print(i)

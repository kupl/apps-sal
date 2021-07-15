s=input()
count=0
for i in range(len(s)):
  if(s[i]=='1'):
    for j in range(i+1,len(s)):
      if(s[j]=='0'):
        count+=1
    break
if(count>=6):
  print("yes")
else:
  print("no")

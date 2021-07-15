num=input()
c=False
for i in range(1,len(num)):
  if num[i]==num[i-1]:
    c=True
    
if c==True:
  print("Bad")
else:
  print("Good")

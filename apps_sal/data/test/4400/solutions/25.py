A=input()
count=0
ma=0
for i in A:
  if i == 'R':
    count+=1
  else:
    count=0
  if count>ma:
    ma = count
print(ma)    

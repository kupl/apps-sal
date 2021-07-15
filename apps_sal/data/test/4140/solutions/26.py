s=input()

start_0=0
start_1=0

for i,j in enumerate(s):
  if i%2==0 and j=="1":
    start_0+=1
  elif i%2!=0 and j=="0":
    start_0+=1
  elif i%2==0 and j=="0":
    start_1+=1
  elif i%2!=0 and j=="1":
    start_1+=1
    
print((min(start_0, start_1)))


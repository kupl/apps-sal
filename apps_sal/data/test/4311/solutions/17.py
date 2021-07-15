s=int(input())
col=[]
a=s
count=1
while True:
  col.append(a) 
  if a%2==0:
    a=a/2
  else:
    a=a*3+1
  if a in col:
    print(count+1)
    break
  count+=1

A,B=map(int,input().split())
result=0
for i in range(A,B+1):
  i=str(i)
  for j in range(int(((len(i))-1)/2)+1):
    if not i[j]==i[-j-1]:
      break
  else:
    result+=1
print(result)

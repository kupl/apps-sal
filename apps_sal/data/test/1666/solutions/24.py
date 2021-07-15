x,y,a,b=[ int(i) for i in input().split() ]

ans=[]
s_a=a
s_b=b
if a<=b:
  s_a=b+1
  s_b=b  

while s_a<=x:
  for i in range(s_b,min(s_a,y+1)):
    ans.append([s_a,i])
  s_a+=1
print(len(ans))
for i in ans:
  print(i[0],i[1])
  
    


K=int(input())
l=[1,2,3,4,5,6,7,8,9]
for i in l:
  if i%10==0:l+=[i*10,i*10+1]
  if i%10==9:l+=[i*10+8,i*10+9]
  if 0<i%10<9:l+=[i*10+(i-1)%10,i*10+i%10,i*10+(i+1)%10]
  if len(l)>10**5:break
print(l[K-1])

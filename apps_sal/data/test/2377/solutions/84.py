n,h=map(int,input().split())
A=[]
B=[]
for i in range(n):
  a,b=map(int,input().split())
  A.append(a)
  B.append(b)
A=max(A)
B.sort(reverse=True)
count=0
for i in B:
  if A>i:
    break
  else:
    if h>0:
      h-=i
      count+=1
    else:
      break
if h%A==0 and h>0:
  print(count+h//A)
elif h%A!=0 and h>0:
  print(count+h//A+1)
else:
  print(count)

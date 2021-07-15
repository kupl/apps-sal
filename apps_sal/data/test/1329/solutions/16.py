sosuu=[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]
N=int(input())
L=[0 for i in range(25)]
for i in range(25):
  s=N
  while True:
    if s!=0:
      s=s//sosuu[i]
      L[i]+=s
    else:
      break
#1 75 3 25 5 15 (3 5 5)
a,b,c,d,e=0,0,0,0,0
for i in range(25):
  if L[i]>=74:
    a+=1
  if L[i]>=24:
    b+=1
  if L[i]>=14:
    c+=1
  if L[i]>=4:
    d+=1
  if L[i]>=2:
    e+=1
print(a+b*(e-1)+c*(d-1)+d*(d-1)*(e-2)//2)

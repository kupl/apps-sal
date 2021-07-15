s="AEIOU"
v=0
c=0
a=3
n=input()
if len(list(set(n)))<8:
 print(-1)
else:    
 for i in range(0,len(n)):
  if i!=len(n)-2:
   k=n[i:i+3]
   if k in s:
    c=c+1
    break
 for y in set(n):
  if y not in s:
   v=v+1
 if v>=5 and c>0:
  print("GOOD")
 else:
  print(-1)

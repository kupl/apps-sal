t=int(input())
for r in range(t):
 q=input()
 a='1'*len(q)
 s=int(a)
 while s<=int(q):
  s+=int(a)
 e=s//int(a)-1
 e+=-9+9*len(q)
 print(e)


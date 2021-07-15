import sys
t = int(sys.stdin.readline())
for i in range(t):
 l = list(map(int,input().split()))
 a,b,c,d = l[0],l[1],l[2],l[3]
 count = 0
 r = 1
 i = a 
 while i<=b:
  if i > d:
   break
  if i<c:
   count = count + d-c+1
  if i>=c:           
   count = count + d-i
  i = i + 1 
 print(count) 
  
 
  

 
   
 


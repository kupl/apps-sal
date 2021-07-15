import sys
ting = int(sys.stdin.readline())
for i in range(ting):
 m = list(map(int,sys.stdin.readline().split()))
 a,b,c,d = m[0],m[1],m[2],m[3]
 count1 = 0
 i = a 
 while i<=b:
  if i > d:
   break
  if i<c:
   count1 = count1 + d-c+1
  if i>=c:           
   count1 = count1 + d-i
  i = i + 1 
 print(count1)
  
 
  

 
   
 


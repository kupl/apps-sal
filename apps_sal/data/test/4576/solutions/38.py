A = int(input())
B = int(input())
C = int(input())
X = int(input())

ans = 0

for i in range(0,A+1):
  a = 500*i
  
  for j in range(0,B+1):
    b = 100*j
    
    for k in range(0,C+1):
      c = 50*k
      
      if a + b + c == X:
        ans += 1
        
print(ans)
  


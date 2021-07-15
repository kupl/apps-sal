n =int(input())
A = list(map(int,input().split()))

B = [0]*n

for i in range(n)[::-1]:
  tmp = 0
  j = i+1
  
  while j<=n:    
    tmp += B[j-1]
    j += i+1
    
  if tmp%2 != A[i]:    
    B[i] = 1

print(sum(B))
print(*[i+1 for i in range(n) if B[i]])

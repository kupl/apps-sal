n,k = list(map(int,input().split()))
A = list(map(int,input().split()))

b = 1
c = 0
while b <= k:
  b *= 2
  c += 1

B = [0]*(c)
for a in A:
  for i in range(c):
    if a>>i & 1 :      
      B[i] += 1
      
x = 0
for b in range(c,-1,-1):
  if x + (1<<b) > k:
    continue
  if B[b] < (n+1)//2:
    x += 1<<b
    
ans = 0
for a in A:
  ans += x^a
print(ans)  


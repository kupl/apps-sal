n = int(input())
A = [0] + list(map(int,  input().split())) + [1001]

c = 0
ans = 0
for i in range(1,n+1):
  if A[i]-1 == A[i-1] and A[i]+1 == A[i+1]:
    c += 1
  else:
    c = 0

  ans = max(ans, c)

print(ans)
 



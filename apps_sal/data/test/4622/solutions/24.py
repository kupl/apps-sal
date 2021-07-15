N = int(input())
A = list(map(int, input().split()))

s=set()
for i in range(N):
  s.add(A[i])
  
if len(s)==N:
  print("YES")
else:
  print("NO")

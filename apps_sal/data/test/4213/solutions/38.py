n=int(input())
ans = 0
A=list(map(int,input().split()))
for i in range(n):
  for j in range(n):
    ans = max(ans,abs(A[i]-A[j]))
print(ans)

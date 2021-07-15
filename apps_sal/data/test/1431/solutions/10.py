N = int(input())
A = list(map(int,input().split()))
B = (N+1)*[0]

for n in range(N,0,-1):
  B[n] = (sum(B[n::n])+A[n-1])%2

print(B.count(1))
for n in range(N+1):
  if B[n]:
    print(n,end=" ")

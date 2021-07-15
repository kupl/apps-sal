N,K=list(map(int,input().split()))
A=list(map(int,input().split()))
m= [0 for i in range(200001) ]
for i in range(N):
  m[A[i]] += 1
m.sort(reverse=True)
ans = 0
for i in range(K,N):
  if ( m[i] == 0 ):  break
  ans += m[i]
print(ans)

